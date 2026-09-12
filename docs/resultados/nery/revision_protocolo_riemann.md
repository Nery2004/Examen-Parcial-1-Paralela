# Revisión de Nery — Protocolo de benchmarking de Riemann

- N pequeño: `10,000,000`.
- N mediano: `100,000,000`.
- N grande: `500,000,000`.
- Configuraciones: secuencial y paralelo con 1, 2, 4 y 8 threads.
- Repeticiones: 5 por configuración.
- Región medida: únicamente el cálculo de la suma y el resultado de la integral.
- Optimización: `-O2` en ambas versiones, con `-std=c++17`, `-Wall`, `-Wextra`
  y `-Wpedantic`.
- Comparación secuencial/paralela válida para Riemann: sí.

Las dos versiones conservan `f(x) = x²`, el intervalo `[0, 1]`, el método del
punto medio, el mismo `N`, el mismo compilador y flags comparables. La versión
secuencial no usa OpenMP; en la paralela los threads se controlan mediante
`OMP_NUM_THREADS`.
