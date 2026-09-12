# Resultados y métricas

## Nery

### Hardware

- Sistema operativo: macOS 26.6.2 (build 25G83).
- Arquitectura: `x86_64`.
- Procesador: Intel Core i9-9980HK @ 2.40 GHz.
- Núcleos físicos: 8.
- Núcleos lógicos: 16.
- RAM: 32 GiB.
- Compilador: Apple Clang++ 21.0.0.
- OpenMP: `libomp` 22.1.8 mediante Homebrew.

### Suma de Riemann — tiempos de ejecución

Todos los tiempos están expresados en segundos y provienen del benchmark individual
de Nery. Cada configuración conserva sus cinco mediciones.

| N | Threads | T1 | T2 | T3 | T4 | T5 | Promedio |
|---:|:---:|---:|---:|---:|---:|---:|---:|
| 10,000,000 | Secuencial | 0.015436979 | 0.015433105 | 0.015492190 | 0.015442946 | 0.015559622 | 0.015472968400 |
| 10,000,000 | 1 | 0.015518011 | 0.015576520 | 0.016088457 | 0.015523627 | 0.015469890 | 0.015635301000 |
| 10,000,000 | 2 | 0.017989152 | 0.007878368 | 0.007813580 | 0.007842067 | 0.007826870 | 0.009870007400 |
| 10,000,000 | 4 | 0.003986120 | 0.004044348 | 0.004030830 | 0.003993594 | 0.004142409 | 0.004039460200 |
| 10,000,000 | 8 | 0.002923838 | 0.002921526 | 0.003433485 | 0.003126247 | 0.002654674 | 0.003011954000 |
| 100,000,000 | Secuencial | 0.156328083 | 0.160603928 | 0.156212129 | 0.155986810 | 0.154806290 | 0.156787448000 |
| 100,000,000 | 1 | 0.155704082 | 0.155200287 | 0.155613331 | 0.156248359 | 0.155043382 | 0.155561888200 |
| 100,000,000 | 2 | 0.078217781 | 0.078077490 | 0.077792660 | 0.077835038 | 0.078265934 | 0.078037780600 |
| 100,000,000 | 4 | 0.039376453 | 0.039262284 | 0.039229337 | 0.039274410 | 0.039968080 | 0.039422112800 |
| 100,000,000 | 8 | 0.027298272 | 0.024103070 | 0.025916117 | 0.023981753 | 0.027024027 | 0.025664647800 |
| 500,000,000 | Secuencial | 0.785260486 | 0.778429644 | 0.777222086 | 0.777505842 | 0.777474010 | 0.779178413600 |
| 500,000,000 | 1 | 0.778035362 | 0.780163363 | 0.777076863 | 0.777617847 | 0.777983403 | 0.778175367600 |
| 500,000,000 | 2 | 0.390506295 | 0.388532213 | 0.389638724 | 0.389893448 | 0.390706782 | 0.389855492400 |
| 500,000,000 | 4 | 0.200188452 | 0.198239806 | 0.195240046 | 0.196778573 | 0.196564941 | 0.197402363600 |
| 500,000,000 | 8 | 0.118044143 | 0.116838838 | 0.117958116 | 0.111740697 | 0.122656577 | 0.117447674200 |

### Suma de Riemann — speedup y eficiencia

Se calcularon `Speedup = Tseq / Tpar` y `Eficiencia = Speedup / threads` a partir
de los promedios anteriores.

| N | Threads | T secuencial (s) | T paralelo (s) | Speedup | Eficiencia | Eficiencia % |
|---:|---:|---:|---:|---:|---:|---:|
| 10,000,000 | 1 | 0.015472968400 | 0.015635301000 | 0.989617558 | 0.989617558 | 98.961756% |
| 10,000,000 | 2 | 0.015472968400 | 0.009870007400 | 1.567675461 | 0.783837730 | 78.383773% |
| 10,000,000 | 4 | 0.015472968400 | 0.004039460200 | 3.830454475 | 0.957613619 | 95.761362% |
| 10,000,000 | 8 | 0.015472968400 | 0.003011954000 | 5.137186159 | 0.642148270 | 64.214827% |
| 100,000,000 | 1 | 0.156787448000 | 0.155561888200 | 1.007878278 | 1.007878278 | 100.787828% |
| 100,000,000 | 2 | 0.156787448000 | 0.078037780600 | 2.009122335 | 1.004561168 | 100.456117% |
| 100,000,000 | 4 | 0.156787448000 | 0.039422112800 | 3.977144726 | 0.994286181 | 99.428618% |
| 100,000,000 | 8 | 0.156787448000 | 0.025664647800 | 6.109082393 | 0.763635299 | 76.363530% |
| 500,000,000 | 1 | 0.779178413600 | 0.778175367600 | 1.001288972 | 1.001288972 | 100.128897% |
| 500,000,000 | 2 | 0.779178413600 | 0.389855492400 | 1.998633927 | 0.999316963 | 99.931696% |
| 500,000,000 | 4 | 0.779178413600 | 0.197402363600 | 3.947158481 | 0.986789620 | 98.678962% |
| 500,000,000 | 8 | 0.779178413600 | 0.117447674200 | 6.634260056 | 0.829282507 | 82.928251% |

### Interpretación de Riemann

Para `N = 10,000,000`, un thread paralelo fue ligeramente más lento que el baseline:
el tiempo pasó de `0.0154729684 s` a `0.015635301 s`, con speedup `0.989617558`.
Esta fila conserva el efecto desfavorable del overhead. Con 8 threads el speedup
subió a `5.137186159`, aunque la eficiencia bajó a `64.214827%`.

Para `N = 100,000,000`, el speedup creció desde `1.007878278` con un thread hasta
`6.109082393` con ocho. Las eficiencias ligeramente superiores al 100% con uno y dos
threads se interpretan como variabilidad de medición y no como evidencia concluyente
de aceleración superlineal.

Para `N = 500,000,000`, ocho threads redujeron el promedio de `0.7791784136 s` a
`0.1174476742 s`, alcanzando el mayor speedup observado: `6.634260056`, con
eficiencia `82.928251%`. Los tamaños mayores amortizaron mejor los costos fijos, pero
la eficiencia disminuyó al aumentar a ocho threads en los tres tamaños.

El mayor speedup corresponde a `N = 500,000,000`, 8 threads: `6.634260056`.
La mayor eficiencia numérica corresponde a `N = 100,000,000`, 1 thread:
`1.007878278` (`100.787828%`), valor afectado por variabilidad temporal.


