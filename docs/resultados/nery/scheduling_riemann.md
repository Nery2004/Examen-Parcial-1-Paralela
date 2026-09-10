# Scheduling de Riemann — Nery

## Estado original

La directiva original era `parallel for reduction(+ : suma)` sin cláusula
`schedule`. Por ello, la política dependía del comportamiento predeterminado del
runtime de OpenMP. El cuerpo del ciclo tiene carga uniforme: cada iteración calcula
un punto medio, evalúa `x²` y actualiza una reducción.

## Configuración

- N: `100,000,000` (carga mediana).
- Threads: 4 y 8.
- Repeticiones: 5 por combinación.
- Compilador y flags: iguales en todas las variantes.
- Chunk size: no se indicó explícitamente.
- Resultado esperado: `1/3`; todos los resultados fueron correctos.

## Mediciones

Todos los tiempos están expresados en segundos.

| Threads | Scheduling | T1 | T2 | T3 | T4 | T5 | Promedio |
|---:|:---:|---:|---:|---:|---:|---:|---:|
| 4 | static | 0.039140479 | 0.039480124 | 0.039793867 | 0.039422659 | 0.039953845 | 0.039558195 |
| 4 | dynamic | 0.997366956 | 0.995594645 | 0.998416180 | 1.033473402 | 1.028131030 | 1.010596443 |
| 8 | static | 0.023844359 | 0.026371794 | 0.025947485 | 0.024227174 | 0.024579284 | 0.024994019 |
| 8 | dynamic | 0.587133117 | 0.672917109 | 0.542912299 | 0.522060883 | 0.529339076 | 0.570872497 |

## Interpretación

`static` tuvo el menor promedio con ambas cantidades de threads. Frente a `static`,
`dynamic` añadió `0.971038248 s` con 4 threads y `0.545878478 s` con 8 threads;
sus promedios fueron respectivamente 25.547 y 22.840 veces mayores. La asignación
dinámica no aporta balance de carga porque las iteraciones tienen costo uniforme y,
sin un chunk explícito, introduce coordinación innecesaria. Se selecciona
`schedule(static)` para la versión final.
