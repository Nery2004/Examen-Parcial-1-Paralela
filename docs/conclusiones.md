# Conclusiones

## Conclusiones — Suma de Riemann

La paralelización con OpenMP fue beneficiosa para las cargas evaluadas cuando se
utilizaron varios threads. La mejor reducción de tiempo se obtuvo con
`N = 500,000,000` y 8 threads: el promedio pasó de `0.7791784136 s` en secuencial
a `0.1174476742 s` en paralelo, con speedup `6.634260056` y eficiencia
`82.928251%`.

El tamaño del problema influyó en la capacidad de amortizar los costos de OpenMP.
Para `N = 10,000,000`, la versión paralela con un thread fue ligeramente más lenta
que el baseline (`0.015635301 s` frente a `0.0154729684 s`), con speedup
`0.989617558`. En las cargas mediana y grande, un thread produjo tiempos muy
similares al secuencial y el beneficio se volvió claro al aumentar el paralelismo.

Dentro de las configuraciones probadas, el tiempo promedio disminuyó al pasar de 1
a 2, 4 y 8 threads. Sin embargo, la eficiencia no creció de la misma manera: con 8
threads fue `64.214827%`, `76.363530%` y `82.928251%` para las cargas pequeña,
mediana y grande. Para equilibrar speedup y utilización de recursos, la carga
mediana con 4 threads obtuvo speedup `3.977144726` y eficiencia `99.428618%`. Esto
muestra que más threads puede reducir el tiempo, pero no garantiza eficiencia
proporcional.

La comparación de scheduling confirmó que `static` es adecuado para este ciclo de
carga uniforme. Con `N = 100,000,000`, `dynamic` promedió `1.010596443 s` con 4
threads y `0.570872497 s` con 8, frente a `0.039558195 s` y `0.024994019 s` con
`static`. La configuración final conserva `schedule(static)` para evitar el overhead
de asignación dinámica y hacer explícita la política utilizada. Este cambio mantuvo
la exactitud numérica; la pequeña reducción observada frente al scheduling implícito
puede incluir variabilidad normal y no se considera por sí sola una aceleración
concluyente.

Los resultados están limitados al equipo de Nery, con 8 núcleos físicos y 16 lógicos,
y a configuraciones de hasta 8 threads. También existió variación entre corridas y
pequeñas diferencias de punto flotante por el orden de la reducción, con una
diferencia máxima validada del orden de `10^-14`. En este alcance, OpenMP sí mejoró
la Suma de Riemann, especialmente cuando `N` proporcionó suficiente trabajo para
compensar la gestión de threads y la reducción final.
