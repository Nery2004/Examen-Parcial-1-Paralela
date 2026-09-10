# Optimización de Riemann — Nery

## Estado inicial

- N: `100,000,000`.
- Threads: 8.
- Scheduling: sin cláusula explícita.
- Resultado: `0.333333333333346`.
- Tiempos: `0.027818222`, `0.025408156`, `0.025570016`, `0.025593121`,
  `0.023466778` s.
- Promedio previo: `0.025571259 s`.

La implementación ya mantenía una sola región paralela, `reduction` para evitar la
condición de carrera, constantes y `dx` fuera del ciclo, cálculo directo de `x` y
memoria adicional `O(1)`. No se identificaron locks, regiones repetidas ni
estructuras de datos innecesarias que justificaran otros cambios.

## Cambio realizado

Se agregó `schedule(static)` explícito a la directiva `parallel for`, conservando
función, intervalo, método, `N`, reducción y control mediante `OMP_NUM_THREADS`.
La carga uniforme permite asignar rangos fijos sin la coordinación por iteración de
`dynamic` y deja la política final explícita y reproducible.

## Medición posterior

- Tiempos: `0.023844359`, `0.026371794`, `0.025947485`, `0.024227174`,
  `0.024579284` s.
- Promedio posterior: `0.024994019 s`.
- Reducción observada: `0.000577239 s` (`2.257%`).
- Resultado: `0.333333333333346`.

La diferencia frente al estado original es pequeña y puede formar parte de la
variabilidad normal, ya que el runtime podía usar una distribución equivalente a
`static` por defecto. No se presenta como una mejora concluyente de velocidad. La
optimización se conserva por reproducibilidad y porque la comparación controlada
mostró un costo mucho mayor para `dynamic`.

## Validación final

| N | Secuencial | Paralelo final | Diferencia absoluta |
|---:|---:|---:|---:|
| 10,000,000 | 0.333333333333298 | 0.333333333333326 | 2.7977620220553945e-14 |
| 100,000,000 | 0.333333333333312 | 0.333333333333346 | 3.4028335704761048e-14 |
| 500,000,000 | 0.333333333333355 | 0.333333333333326 | 2.9032332093947844e-14 |

La exactitud se conserva dentro de las diferencias esperadas por el orden de las
operaciones de punto flotante.
