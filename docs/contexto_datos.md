# Contexto y datos

## Suma de Riemann

### Descripción del problema

La suma de Riemann aproxima una integral definida dividiendo un intervalo en `N`
subintervalos de ancho uniforme. En cada subintervalo se evalúa la función y se
acumula el área aproximada. Este problema es útil en HPC porque realiza muchas
iteraciones con contribuciones independientes; la acumulación final, sin embargo,
requiere cuidado cuando participan varios threads.

### Propuesta secuencial

La implementación calcula `dx = (b - a) / N` una sola vez. Para cada índice `i`
obtiene el punto medio `x = a + (i + 0.5) * dx`, evalúa `f(x)` y acumula el valor en
una variable `double`. Al terminar multiplica la suma por `dx`. `N` se recibe como
argumento de línea de comandos, se valida como entero positivo de tipo `long long`
y usa `1,000,000` si se omite. `std::chrono::steady_clock` mide únicamente el
cálculo de la integral.

### Función e intervalo

- Función utilizada: `f(x) = x²`.
- Intervalo: `[0, 1]`.
- Valor exacto de referencia: `1/3`.

### Método utilizado

Se utiliza la regla del punto medio. La función se evalúa en el centro de cada
subintervalo, no en sus extremos izquierdo o derecho.

### Datos de prueba

| Nivel | N | Propósito |
|---|---:|---|
| Pequeño | 10,000,000 | Observar el peso relativo del overhead cuando hay poco trabajo. |
| Mediano | 100,000,000 | Representar una carga intermedia y medible. |
| Grande | 500,000,000 | Evaluar mejor la escalabilidad con suficiente trabajo computacional. |

### Justificación de los tamaños

En las pruebas preliminares, `N = 1,000,000` tardó aproximadamente `0.00166 s`,
un intervalo demasiado breve para mediciones estables. Por ello se seleccionaron
`10,000,000`, `100,000,000` y `500,000,000`. Los tres niveles permiten estudiar
el efecto del tamaño, el overhead y el comportamiento al aumentar threads sin hacer
imprácticas las repeticiones.

### Estructuras utilizadas en memoria

No se almacenan los puntos `x` ni los valores `f(x)` en arreglos o vectores. Cada
iteración utiliza variables escalares y contribuye a un único acumulador. El consumo
adicional de memoria es constante, `O(1)`, independientemente de `N`.

### Complejidad aproximada

El trabajo crece linealmente con las subdivisiones, por lo que la complejidad
temporal es `O(N)` y la memoria adicional es `O(1)`.
