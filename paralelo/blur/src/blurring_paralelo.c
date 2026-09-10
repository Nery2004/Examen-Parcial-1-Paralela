// se corre: 
// ./blurring_paralelo ../../../data/blur/pequena.bmp   ../../../data/blur/salida_par_pequena.bmp

#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main(int argc, char *argv[]) {
    // Ruta de entrada y salida configurables por línea de comandos, para
    // poder probar las 3 imágenes (pequeña/mediana/grande) de data/blur/
    // sin recompilar. Si no se pasan argumentos, se usan estos valores
    // por defecto:
    const char *ruta_entrada = "../../../data/blur/pequena.bmp";
    const char *ruta_salida  = "../../../data/blur/resultado_blur.bmp";

    if (argc >= 2) ruta_entrada = argv[1];
    if (argc >= 3) ruta_salida  = argv[2];

    // abrir imagen original y preparar la de salida
    FILE *archivo_entrada = fopen(ruta_entrada, "rb");
    FILE *archivo_salida = fopen(ruta_salida, "wb");

    if (!archivo_entrada || !archivo_salida) {
        printf("Error al abrir los archivos. Verifica la ruta: %s\n", ruta_entrada);
        return 1;
    }

    // cabeceras del archivo BMP
    unsigned char cabecera[54];
    fread(cabecera, sizeof(unsigned char), 54, archivo_entrada);
    fwrite(cabecera, sizeof(unsigned char), 54, archivo_salida);

    // leer dimensiones de la imagen desde la cabecera
    int ancho = *(int*)&cabecera[18];
    int alto = *(int*)&cabecera[22];
    if (alto < 0) alto = -alto;

    // Matrices de entrada: se leen durante el blur, nunca se escriben ahí -> son solo lectura
    unsigned char **rojo = malloc(alto * sizeof(unsigned char*));
    unsigned char **verde = malloc(alto * sizeof(unsigned char*));
    unsigned char **azul = malloc(alto * sizeof(unsigned char*));

    // Matrices de salida: cada hilo escribe únicamente su propia fila "y"
    unsigned char **rojo_out = malloc(alto * sizeof(unsigned char*));
    unsigned char **verde_out = malloc(alto * sizeof(unsigned char*));
    unsigned char **azul_out = malloc(alto * sizeof(unsigned char*));

    for (int i = 0; i < alto; i++) {
        rojo[i] = malloc(ancho);
        verde[i] = malloc(ancho);
        azul[i] = malloc(ancho);
        rojo_out[i] = malloc(ancho);
        verde_out[i] = malloc(ancho);
        azul_out[i] = malloc(ancho);
    }

    int padding = (4 - (ancho * 3) % 4) % 4;

    // Lectura: obligatoriamente secuencial 
    // fread/fgetc/fseek avanzan un cursor compartido del archivo; si varios
    // hilos leen a la vez, el orden de los bytes se pierde. No conviene
    // paralelizar este ciclo.
    for (int y = 0; y < alto; y++) {
        for (int x = 0; x < ancho; x++) {
            azul[y][x] = fgetc(archivo_entrada);
            verde[y][x] = fgetc(archivo_entrada);
            rojo[y][x] = fgetc(archivo_entrada);
        }
        fseek(archivo_entrada, padding, SEEK_CUR);
    }

    // Región paralela
    // Se paraleliza por filas (ciclo en "y"). Cada iteración es independiente:
    // solo lee de rojo/verde/azul (matrices originales, que nadie modifica
    // durante esta región) y solo escribe en su propia fila de
    // rojo_out/verde_out/azul_out. Como ningún hilo escribe una posición que
    // otro hilo también escribe, no hay condición de carrera: no se necesita
    // "critical" ni "atomic".
    //
    // Se usa schedule(runtime) para poder probar static vs dynamic sin
    // recompilar.
    #pragma omp parallel for schedule(runtime)
    for (int y = 0; y < alto; y++) {
        for (int x = 0; x < ancho; x++) {

            // Bordes: se copian igual que en la versión secuencial, sin promediar
            if (y == 0 || y == alto - 1 || x == 0 || x == ancho - 1) {
                azul_out[y][x] = azul[y][x];
                verde_out[y][x] = verde[y][x];
                rojo_out[y][x] = rojo[y][x];
                continue;
            }

            int sumaR = 0, sumaG = 0, sumaB = 0;

            for (int dy = -1; dy <= 1; dy++) {
                for (int dx = -1; dx <= 1; dx++) {
                    sumaR += rojo[y + dy][x + dx];
                    sumaG += verde[y + dy][x + dx];
                    sumaB += azul[y + dy][x + dx];
                }
            }

            rojo_out[y][x]  = sumaR / 9;
            verde_out[y][x] = sumaG / 9;
            azul_out[y][x]  = sumaB / 9;
        }
    }
    // Fin región paralela 

    // Escritura: obligatoriamente secuencial, por la misma razón que la lectura 
    for (int y = 0; y < alto; y++) {
        for (int x = 0; x < ancho; x++) {
            fputc(azul_out[y][x], archivo_salida);
            fputc(verde_out[y][x], archivo_salida);
            fputc(rojo_out[y][x], archivo_salida);
        }
        for (int p = 0; p < padding; p++) {
            fputc(0, archivo_salida);
        }
    }

    // liberar memoria
    for (int i = 0; i < alto; i++) {
        free(rojo[i]); free(verde[i]); free(azul[i]);
        free(rojo_out[i]); free(verde_out[i]); free(azul_out[i]);
    }
    free(rojo); free(verde); free(azul);
    free(rojo_out); free(verde_out); free(azul_out);

    fclose(archivo_entrada);
    fclose(archivo_salida);

    printf("Imagen desenfocada con exito (version paralela)!\n");
    return 0;
}
