# Revisión cruzada — Nery

## Blur de Renato

| Verificación | Estado |
|---|---|
| Secuencial compila | No: implementación ausente |
| Paralelo compila | No: implementación ausente |
| OpenMP correcto | No verificable |
| Race conditions evidentes | No verificable |
| Índices | No verificable |
| Bordes correctos | No verificable |
| Lectura y escritura separadas | No verificable |
| Resultado de salida | No verificable |

`secuencial/blur/`, `paralelo/blur/` y `data/blur/` contienen únicamente archivos
`.gitkeep`. Nery no modificó ni intentó reemplazar la implementación de Renato.

## Documentación de Blur

No existen secciones de Blur en `docs/contexto_datos.md`,
`docs/estrategia_paralelizacion.md`, `docs/resultados_metricas.md` o
`docs/conclusiones.md`. Por ello no es posible contrastar función, imágenes,
resoluciones, memoria, OpenMP, scheduling o resultados contra el código.

## Resultados de Riemann de otros integrantes

- Abby: `docs/resultados/abby/` no existe; no hay resultados para revisar.
- Renato: `docs/resultados/renato/` no existe; no hay resultados para revisar.

## Coherencia general de Riemann

| Verificación | Estado |
|---|---|
| Función `f(x) = x²` | Consistente en la documentación de Nery |
| Intervalo `[0, 1]` | Consistente en la documentación de Nery |
| Método del punto medio | Consistente en la documentación de Nery |
| N: 10M, 100M y 500M | Consistentes en la documentación de Nery |
| Métricas | Consistentes con los promedios del benchmark de Nery |
| Scheduling final `static` | Consistente con el código y las mediciones de Nery |

No puede comprobarse coherencia entre integrantes porque faltan los resultados de
Riemann de Abby y Renato.

## Problemas encontrados

### 1. Implementación y datos de Blur ausentes

- Gravedad: **CRÍTICO**.
- Archivos: `secuencial/blur/`, `paralelo/blur/`, `data/blur/`.
- Descripción: no hay código ni imágenes; Blur no puede compilarse o validarse.
- Solución sugerida: Renato debe incorporar y validar ambas versiones junto con las
  imágenes oficiales antes de la validación final.

### 2. Documentación de Blur ausente

- Gravedad: **IMPORTANTE**.
- Archivos: `docs/contexto_datos.md`, `docs/estrategia_paralelizacion.md`,
  `docs/resultados_metricas.md`, `docs/conclusiones.md`.
- Descripción: no existen secciones que puedan contrastarse contra Blur.
- Solución sugerida: Renato debe redactar sus secciones y Abby debe integrarlas sin
  alterar la parte de Riemann.

### 3. Resultados de Riemann de Abby ausentes

- Gravedad: **CRÍTICO**.
- Archivo: `docs/resultados/abby/`.
- Descripción: la carpeta no existe y no hay mediciones individuales para revisar.
- Solución sugerida: Abby debe ejecutar y guardar sus pruebas oficiales de Riemann.

### 4. Resultados de Riemann de Renato ausentes

- Gravedad: **CRÍTICO**.
- Archivo: `docs/resultados/renato/`.
- Descripción: la carpeta no existe y no hay mediciones individuales para revisar.
- Solución sugerida: Renato debe ejecutar y guardar sus pruebas oficiales de Riemann.

### 5. Evidencias de Nery insuficientes

- Gravedad: **IMPORTANTE**.
- Archivo: `docs/screenshots/nery/`.
- Descripción: no hay capturas reales de Riemann o Blur; solo existía `.gitkeep`.
- Solución sugerida: Nery debe capturar ejecuciones auténticas donde sean visibles el
  algoritmo, N, threads, resultado y tiempo, sin editar los valores.
