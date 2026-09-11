#correr todos los programas y analizar resutlados de estos
"""
Se genera en /resultados/<timestamp>:
    - tiempos.csv
    - speedup.csv
    - eficiencia.csv
    - resumen.txt
    - grafica_tiempos_riemann.png
    - grafica_speedup_riemann.png
    - grafica_eficiencia_riemann.png
    - grafica_tiempos_blur.png
    - grafica_speedup_blur.png
    - grafica_eficiencia_blur.png
"""

import argparse
import csv
import os
import shutil
import statistics
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent

RUTAS = {
    "blur_sec":   RAIZ / "secuencial" / "blur" / "src" / "blurring_secuencial.c",
    "blur_par":   RAIZ / "paralelo"   / "blur" / "src" / "blurring_paralelo.c",
    "riem_sec":   RAIZ / "secuencial" / "riemann" / "src" / "riemann_secuencial.cpp",
    "riem_par":   RAIZ / "paralelo"   / "riemann" / "src" / "riemann_paralelo.cpp",
}
BIN_DIR = RAIZ / "bin"
RES_DIR = RAIZ / "docs" / "resultados" / "resultados_analisis"

#tamaños e imagnes
N_RIEMANN = [10_000_000, 50_000_000, 100_000_000, 500_000_000]
IMAGENES_BLUR = {
    "pequena": RAIZ / "data" / "blur" / "pequena.bmp",
    "mediana": RAIZ / "data" / "blur" / "mediana.bmp",
    "grande":  RAIZ / "data" / "blur" / "grande.bmp",
}

HILOS = [1, 2, 4, 8]

REPS = 3 #repetciones/medicion

def log(msg: str) -> None:
    print(f"[benchmark] {msg}", flush=True)


def compilar_programa(ruta_fuente: Path, salida: Path, es_cpp: bool, con_omp: bool) -> None:
    #compilaciones de archvios cpp y c
    if not ruta_fuente.exists():
        raise FileNotFoundError(f"No existe el fuente: {ruta_fuente}")

    compilador = "g++" if es_cpp else "gcc"
    cmd = [compilador, "-O2", "-o", str(salida), str(ruta_fuente)]
    if con_omp:
        cmd.insert(2, "-fopenmp")

    log(f"Compilando {ruta_fuente.name} -> {salida.name}")
    subprocess.run(cmd, check=True)


def compilar_todo() -> dict:
    #compilacion simultanea
    BIN_DIR.mkdir(exist_ok=True)

    binarios = {
        "blur_sec": BIN_DIR / "blurring_secuencial",
        "blur_par": BIN_DIR / "blurring_paralelo",
        "riem_sec": BIN_DIR / "riemann_secuencial",
        "riem_par": BIN_DIR / "riemann_paralelo",
    }

    compilar_programa(RUTAS["blur_sec"], binarios["blur_sec"], es_cpp=False, con_omp=False)
    compilar_programa(RUTAS["blur_par"], binarios["blur_par"], es_cpp=False, con_omp=True)
    compilar_programa(RUTAS["riem_sec"], binarios["riem_sec"], es_cpp=True,  con_omp=False)
    compilar_programa(RUTAS["riem_par"], binarios["riem_par"], es_cpp=True,  con_omp=True)

    return binarios


def correr_programas(cmd: list, env_extra: dict = None) -> tuple:
    env = os.environ.copy()
    if env_extra:
        env.update(env_extra)

    t0 = time.perf_counter()
    proc = subprocess.run(cmd, capture_output=True, text=True, env=env)
    t1 = time.perf_counter()

    if proc.returncode != 0:
        raise RuntimeError(
            f"Comando falló: {' '.join(cmd)}\n"
            f"stdout: {proc.stdout}\n"
            f"stderr: {proc.stderr}"
        )
    return proc.stdout, proc.stderr, (t1 - t0)


def medir_metricas(cmd: list, env_extra: dict, reps: int) -> float:
    #media tiempo
    tiempos = []
    for _ in range(reps):
        _, _, t = correr_programas(cmd, env_extra)
        tiempos.append(t)
    return statistics.median(tiempos)


#RIEMMAN
def parsear_tiempo_riemann(stdout: str) -> float:
    for linea in stdout.splitlines():
        if linea.startswith("Tiempo:"):
            return float(linea.split(":", 1)[1].strip().split()[0])
    raise ValueError(f"No se encontró 'Tiempo:' en:\n{stdout}")


def benchmark_riemann(binarios: dict, reps: int, hilos: list) -> list:
    #lista dics riedmann
    filas = []

    for n in N_RIEMANN:
        log(f"Riemann: N = {n:,}")

        #secuencial
        t_sec = medir_metricas([str(binarios["riem_sec"]), str(n)], {}, reps)
        filas.append({
            "programa": "riemann",
            "variante": "secuencial",
            "N": n,
            "imagen": "",
            "hilos": 1,
            "tiempo_mediana": t_sec,
        })

        #paralelo
        for h in hilos:
            t_par = medir_metricas(
                [str(binarios["riem_par"]), str(n)],
                {"OMP_NUM_THREADS": str(h)},
                reps,
            )
            filas.append({
                "programa": "riemann",
                "variante": "paralelo",
                "N": n,
                "imagen": "",
                "hilos": h,
                "tiempo_mediana": t_par,
            })

    return filas


#BLUR
def benchmark_blur(binarios: dict, reps: int, hilos: list) -> list:
    filas = []
    salida_tmp = BIN_DIR / "salida_tmp.bmp"

    for nombre_img, ruta_img in IMAGENES_BLUR.items():
        if not ruta_img.exists():
            log(f"AVISO: no existe {ruta_img}, se omite")
            continue

        log(f"Blur: imagen = {nombre_img}")

        #Secuencial
        t_sec = medir_metricas(
            [str(binarios["blur_sec"]), str(ruta_img), str(salida_tmp)],
            {},
            reps,
        )
        filas.append({
            "programa": "blur",
            "variante": "secuencial",
            "N": 0,
            "imagen": nombre_img,
            "hilos": 1,
            "tiempo_mediana": t_sec,
        })

        #Paralelo
        for h in hilos:
            t_par = medir_metricas(
                [str(binarios["blur_par"]), str(ruta_img), str(salida_tmp)],
                {"OMP_NUM_THREADS": str(h)},
                reps,
            )
            filas.append({
                "programa": "blur",
                "variante": "paralelo",
                "N": 0,
                "imagen": nombre_img,
                "hilos": h,
                "tiempo_mediana": t_par,
            })

    return filas


#speedup, eficiencia

def calcular_metricas(filas: list) -> list:
    #speedup y eficiencia a cada fila paralela
    secuenciales = {}
    for f in filas:
        if f["variante"] == "secuencial":
            clave = (f["programa"], f["N"], f["imagen"])
            secuenciales[clave] = f["tiempo_mediana"]

    resultados = []
    for f in filas:
        if f["variante"] == "secuencial":
            f["speedup"] = 1.0
            f["eficiencia"] = 1.0
            resultados.append(f)
            continue

        clave = (f["programa"], f["N"], f["imagen"])
        t_sec = secuenciales.get(clave)
        if t_sec is None:
            continue

        speedup = t_sec / f["tiempo_mediana"]
        eficiencia = speedup / f["hilos"]
        f["speedup"] = speedup
        f["eficiencia"] = eficiencia
        resultados.append(f)

    return resultados


#grficas
def graficar(resultados: list, out_dir: Path) -> None:
    #reimann
    riemann = [f for f in resultados if f["programa"] == "riemann"]
    ns = sorted({f["N"] for f in riemann})

    for metrica, ylabel, fname in [
        ("tiempo_mediana", "Tiempo (s)", "grafica_tiempos_riemann.png"),
        ("speedup",        "Speedup",    "grafica_speedup_riemann.png"),
        ("eficiencia",     "Eficiencia", "grafica_eficiencia_riemann.png"),
    ]:
        fig, ax = plt.subplots(figsize=(8, 5))
        for n in ns:
            serie = sorted(
                [f for f in riemann if f["N"] == n],
                key=lambda x: x["hilos"],
            )
            xs = [f["hilos"] for f in serie]
            ys = [f[metrica] for f in serie]
            ax.plot(xs, ys, marker="o", label=f"N = {n:,}")

        if metrica == "speedup":
            maxh = max(f["hilos"] for f in riemann)
            ax.plot([1, maxh], [1, maxh], "k--", alpha=0.4, label="ideal")
        if metrica == "eficiencia":
            ax.axhline(1.0, color="k", linestyle="--", alpha=0.4, label="ideal")

        ax.set_xlabel("Hilos")
        ax.set_ylabel(ylabel)
        ax.set_title(f"Riemann - {ylabel}")
        ax.set_xticks(sorted({f["hilos"] for f in riemann}))
        ax.grid(True, alpha=0.3)
        ax.legend()
        fig.tight_layout()
        fig.savefig(out_dir / fname, dpi=120)
        plt.close(fig)

    #blur
    blur = [f for f in resultados if f["programa"] == "blur"]
    imagenes = sorted({f["imagen"] for f in blur})

    for metrica, ylabel, fname in [
        ("tiempo_mediana", "Tiempo (s)", "grafica_tiempos_blur.png"),
        ("speedup",        "Speedup",    "grafica_speedup_blur.png"),
        ("eficiencia",     "Eficiencia", "grafica_eficiencia_blur.png"),
    ]:
        fig, ax = plt.subplots(figsize=(8, 5))
        for img in imagenes:
            serie = sorted(
                [f for f in blur if f["imagen"] == img],
                key=lambda x: x["hilos"],
            )
            xs = [f["hilos"] for f in serie]
            ys = [f[metrica] for f in serie]
            ax.plot(xs, ys, marker="s", label=img)

        if metrica == "speedup":
            maxh = max(f["hilos"] for f in blur)
            ax.plot([1, maxh], [1, maxh], "k--", alpha=0.4, label="ideal")
        if metrica == "eficiencia":
            ax.axhline(1.0, color="k", linestyle="--", alpha=0.4, label="ideal")

        ax.set_xlabel("Hilos")
        ax.set_ylabel(ylabel)
        ax.set_title(f"Blur - {ylabel}")
        ax.set_xticks(sorted({f["hilos"] for f in blur}))
        ax.grid(True, alpha=0.3)
        ax.legend()
        fig.tight_layout()
        fig.savefig(out_dir / fname, dpi=120)
        plt.close(fig)



def escribir_csv(resultados: list, out_dir: Path) -> None:
    columnas = ["programa", "variante", "N", "imagen", "hilos",
                "tiempo_mediana", "speedup", "eficiencia"]

    with open(out_dir / "tiempos.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=columnas)
        w.writeheader()
        for fila in resultados:
            w.writerow(fila)

def escribir_resumen(resultados: list, out_dir: Path, integrante: str) -> None:
    lineas = []
    lineas.append("=" * 70)
    lineas.append("RESUMEN BENCHMARK")
    lineas.append("=" * 70)
    lineas.append(f"Integrante : {integrante}")
    lineas.append(f"Fecha      : {datetime.now().isoformat(timespec='seconds')}")
    lineas.append(f"Repeticiones/medicion: {REPS} (se reporta la mediana)")
    lineas.append(f"Hilos probados: {HILOS}")
    lineas.append(f"N (riemann): {N_RIEMANN}")
    lineas.append(f"Imagenes (blur): {list(IMAGENES_BLUR.keys())}")
    lineas.append("")

    # Riemann
    lineas.append("-" * 70)
    lineas.append("RIEMANN (integral de x^2 en [0,1])")
    lineas.append("-" * 70)
    lineas.append(f"{'N':>15} {'hilos':>6} {'tiempo(s)':>12} "
                  f"{'speedup':>10} {'eficiencia':>12}")
    for f in sorted([x for x in resultados if x["programa"] == "riemann"],
                    key=lambda x: (x["N"], x["hilos"])):
        lineas.append(
            f"{f['N']:>15,} {f['hilos']:>6} {f['tiempo_mediana']:>12.6f} "
            f"{f['speedup']:>10.3f} {f['eficiencia']:>12.3f}"
        )
    lineas.append("")
    # Blur
    lineas.append("-" * 70)
    lineas.append("BLUR (filtro 3x3)")
    lineas.append("-" * 70)
    lineas.append(f"{'imagen':>10} {'hilos':>6} {'tiempo(s)':>12} "
                  f"{'speedup':>10} {'eficiencia':>12}")
    for f in sorted([x for x in resultados if x["programa"] == "blur"],
                    key=lambda x: (x["imagen"], x["hilos"])):
        lineas.append(
            f"{f['imagen']:>10} {f['hilos']:>6} {f['tiempo_mediana']:>12.6f} "
            f"{f['speedup']:>10.3f} {f['eficiencia']:>12.3f}"
        )
    lineas.append("")
    lineas.append("=" * 70)

    texto = "\n".join(lineas)
    print(texto)
    with open(out_dir / "resumen.txt", "w") as f:
        f.write(texto + "\n")

def nom_integrante() -> str:
    while True:
        nombre = input("Nombre integrante: ").strip()
        if nombre:
            return nombre
        print(" El nombre no puede estar vacio. Intente de nuevo.")


def main():
    global REPS, HILOS, N_RIEMANN

    parser = argparse.ArgumentParser(description="Benchmark blur + riemann")
    parser.add_argument("--rapido", action="store_true", help="Config reducida para pruebas rapidas")
    parser.add_argument("--integrante", type=str, default=None, help="Nombre integrante. Si no se pasa, se pide por input.")
    args = parser.parse_args()

    if args.rapido:
        REPS = 1
        HILOS = [1, 2, 4]
        N_RIEMANN = [1_000_000, 5_000_000, 10_000_000]

    if args.integrante:
        integrante = args.integrante.strip() or "anonimo"
    else:
        integrante = nom_integrante()

    #carpetas resutlados
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = RES_DIR / f"{timestamp}_{integrante}"
    out_dir.mkdir(parents=True, exist_ok=True)
    log(f"Resultados en: {out_dir}")

    try:
        binarios = compilar_todo()
    except Exception as e:
        log(f"ERROR compilando: {e}")
        sys.exit(1)

    #corer benchmark
    resultados = []
    resultados += benchmark_riemann(binarios, REPS, HILOS)
    resultados += benchmark_blur(binarios, REPS, HILOS)

    resultados = calcular_metricas(resultados)

    escribir_csv(resultados, out_dir)
    escribir_resumen(resultados, out_dir, integrante)

    try:
        graficar(resultados, out_dir)
        log("Graficas generadas")
    except Exception as e:
        log(f"ERROR: no se pudieron generar graficas: {e}")

    log(f"Procesos finalizados\n\t{out_dir}")


if __name__ == "__main__":
    main()