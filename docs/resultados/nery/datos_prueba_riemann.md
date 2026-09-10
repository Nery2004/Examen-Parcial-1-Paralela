# Datos de prueba — Suma de Riemann

## Configuración del algoritmo

- Función: `f(x) = x²`.
- Intervalo: `[0, 1]`.
- Método: suma de Riemann por punto medio.
- Tipo de dato de `N`: `long long`.
- Tipo de dato de los cálculos: `double`.
- Definición de `N`: argumento de línea de comandos; si se omite, el valor predeterminado es `1,000,000`.

## Tamaños seleccionados

Los tiempos siguientes provienen de una sola ejecución secuencial por tamaño en el
entorno de Nery. Son pruebas preliminares para seleccionar las cargas, no resultados
de un benchmark oficial.

### Carga pequeña

- N: `10,000,000`.
- Tiempo preliminar: `0.0154431 s`.

Este tamaño reemplaza la propuesta inicial de `1,000,000`, cuyo tiempo preliminar
fue de apenas `0.001662681 s`. Conserva una ejecución breve y permitirá estudiar
posteriormente si el costo de crear y coordinar threads resulta significativo frente
al trabajo útil.

### Carga mediana

- N: `100,000,000`.
- Tiempo preliminar: `0.15689023 s`.

Produce aproximadamente un orden de magnitud más de trabajo que la carga pequeña,
pero continúa siendo manejable. Sirve como punto intermedio para observar cómo el
tamaño del problema afecta la capacidad de aprovechar múltiples threads.

### Carga grande

- N: `500,000,000`.
- Tiempo preliminar: `0.775939592 s`.

Genera una carga computacional claramente mayor y un tiempo medible, sin hacer
imprácticas las repeticiones de una etapa posterior. Permitirá estudiar escalabilidad
y si una carga grande amortiza mejor el overhead de paralelización.

## Estructuras utilizadas en memoria

La implementación no almacena las subdivisiones ni utiliza arreglos o vectores. En
cada iteración calcula directamente `x` y `f(x)`, y acumula el valor en una única
variable `double`. Por ello, el uso adicional de memoria es constante, `O(1)`, y no
crece con `N`.

## Criterio de selección

Los tres tamaños representan cargas separadas de forma clara y mantienen tiempos
manejables en el hardware actual. Esta selección permitirá estudiar posteriormente
el efecto del tamaño del problema, el overhead de OpenMP y la escalabilidad al variar
la cantidad de threads. No se presupone que la ejecución paralela será más rápida;
eso deberá comprobarse con el protocolo de benchmarking correspondiente.
