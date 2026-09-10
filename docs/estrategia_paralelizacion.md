# Estrategia de paralelización

## Suma de Riemann

### Región paralelizada

Se paralelizó el ciclo que recorre las `N` subdivisiones. Cada iteración calcula un
punto medio y su contribución `f(x)` de forma independiente, por lo que las
iteraciones pueden distribuirse entre threads.

### Directivas OpenMP

La versión final utiliza:

```cpp
#pragma omp parallel for reduction(+ : suma) schedule(static)
```

`parallel for` crea el equipo de threads y reparte las iteraciones del ciclo. OpenMP
solo se usa en la versión paralela; el baseline secuencial no depende de la biblioteca.

### Race condition

Aunque cada `x` se calcula independientemente, todos los threads necesitan contribuir
al acumulador `suma`. Una actualización concurrente sin protección podría perder
operaciones y producir un resultado no determinista.

### Uso de reduction

`reduction(+ : suma)` proporciona a cada thread un acumulador parcial privado. Al
finalizar el ciclo, OpenMP combina automáticamente las sumas parciales mediante la
operación `+`. Esto evita la condición de carrera sin serializar cada iteración con
una sección crítica.

### Variables compartidas y privadas

- `n`, `dx` y los límites del intervalo son compartidos y se usan solo para lectura.
- El índice `i` del ciclo es privado por definición de `parallel for`.
- `x` se declara dentro del cuerpo del ciclo y es privado para cada iteración.
- `suma` participa en la reducción: cada thread usa una copia parcial que se combina
  al finalizar.

### Scheduling

Se compararon `schedule(static)` y `schedule(dynamic)` con `N = 100,000,000`, 4 y
8 threads, y cinco repeticiones por combinación.

| Threads | Promedio static (s) | Promedio dynamic (s) |
|---:|---:|---:|
| 4 | 0.039558195 | 1.010596443 |
| 8 | 0.024994019 | 0.570872497 |

`static` tuvo menor tiempo en ambos casos. `dynamic` fue 25.547 veces más lento con
4 threads y 22.840 veces más lento con 8 threads. La versión final conserva
`schedule(static)` explícito.

### Balance de carga

Todas las iteraciones ejecutan las mismas operaciones básicas, por lo que la carga
es homogénea. Una distribución estática asignada al inicio es suficiente y evita la
coordinación repetida del scheduling dinámico.

### Overhead

La ejecución paralela incluye creación y gestión del equipo, distribución del ciclo
y combinación de la reducción. En el benchmark pequeño, la versión paralela con un
thread promedió `0.015635301 s`, frente a `0.0154729684 s` del baseline, lo cual
produjo speedup `0.989617558` y evidencia un overhead pequeño pero medible.

### Control del número de threads

La cantidad se controla con `OMP_NUM_THREADS`; se probaron 1, 2, 4 y 8 threads.
`omp_set_dynamic(0)` evita que el runtime reduzca dinámicamente el equipo solicitado,
y no se fija permanentemente una cantidad de threads en el código.

### Optimización final

Se hizo explícito `schedule(static)` después de la comparación controlada. La función,
el intervalo, el método del punto medio, `N` y la reducción permanecieron sin cambios.
No se añadieron arreglos, locks ni regiones paralelas adicionales.
