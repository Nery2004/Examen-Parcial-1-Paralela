# Validación de Suma de Riemann

## Configuración

- Función: `f(x) = x²`.
- Intervalo: `[0, 1]`.
- Método: suma de Riemann por punto medio.
- Valor matemático esperado: `1/3`.
- Versión paralela: OpenMP con `parallel for` y `reduction(+ : suma)`.
- Control de threads: variable de entorno `OMP_NUM_THREADS`.
- Scheduling: comportamiento predeterminado de OpenMP, sin cláusula `schedule` explícita.

## Estrategia paralela

Cada iteración calcula un punto medio independiente, por lo que el ciclo puede
distribuirse entre threads. Sin una reducción, las actualizaciones simultáneas del
acumulador `suma` producirían una condición de carrera. La cláusula `reduction`
proporciona acumuladores parciales privados y combina sus valores al terminar.

- Compartidas y de solo lectura: `n`, `dx` y los límites del intervalo.
- Privadas: el índice `i` y el valor `x` declarado dentro de cada iteración.
- Reducción: `suma` es privada parcialmente y se combina mediante suma.

## Comparación

La versión paralela se ejecutó con 4 threads para esta comparación funcional.

| N | Secuencial | Paralelo | Diferencia absoluta |
|---:|---:|---:|---:|
| 10,000,000 | 0.333333333333298 | 0.333333333333334 | 3.5971225997855072e-14 |
| 100,000,000 | 0.333333333333312 | 0.333333333333334 | 2.19824158875781e-14 |
| 500,000,000 | 0.333333333333355 | 0.333333333333294 | 6.1006755203152352e-14 |

## Prueba por threads

Se utilizó `N = 10,000,000`. Cada configuración se ejecutó una sola vez para
comprobar funcionalidad; estos datos no constituyen un benchmark oficial.

| Threads | Resultado | Correcto |
|---:|---:|:---:|
| 1 | 0.333333333333298 | Sí |
| 2 | 0.333333333333329 | Sí |
| 4 | 0.333333333333334 | Sí |
| 8 | 0.333333333333326 | Sí |

## Conclusión de validación

Las versiones secuencial y paralela producen resultados equivalentes dentro de las
pequeñas diferencias esperadas por el orden de las operaciones de punto flotante.
Todos los resultados también son coherentes con el valor matemático `1/3`. No se
observaron valores `NaN`, infinitos, resultados nulos, crashes ni variaciones que
sugieran una condición de carrera.
