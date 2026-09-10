# Evidencias de ejecución — Nery

Las siguientes capturas provienen de ejecuciones reales con `N = 500000000`.
Estos tiempos documentan la evidencia visual y no sustituyen los resultados del
benchmark oficial.

| Archivo | Algoritmo | N | Threads | Resultado | Tiempo | Evidencia |
|---|---|---:|:---:|---:|---:|---|
| `riemann_500000000_secuencial.png` | Suma de Riemann | 500000000 | Secuencial | 0.333333333333355 | 0.772312955 s | Ejecución secuencial real |
| `riemann_500000000_2threads.png` | Suma de Riemann | 500000000 | 2 | 0.333333333333275 | 0.386340598 s | Ejecución paralela real |
| `riemann_500000000_4threads.png` | Suma de Riemann | 500000000 | 4 | 0.333333333333294 | 0.19859591 s | Ejecución paralela real |
| `riemann_500000000_8threads.png` | Suma de Riemann | 500000000 | 8 | 0.333333333333326 | 0.119902034 s | Ejecución paralela real |
