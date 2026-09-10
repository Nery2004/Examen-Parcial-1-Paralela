# Plan de trabajo — Parcial 1 de Computación Paralela y Distribuida

## Equipo
- **Nery**
- **Renato**
- **Abby**

## Temas seleccionados
1. **Suma de Riemann**
2. **Blur de imágenes**

## Responsables principales

- **Nery:** Suma de Riemann.
- **Renato:** Blur de imágenes.
- **Abby:** Integración, benchmarking, optimización, consolidación de resultados y revisión general.

> **Importante:** aunque cada integrante tenga una responsabilidad principal, los tres deben ejecutar pruebas, obtener métricas propias y guardar evidencia de sus ejecuciones.

> **Regla del equipo:** no modificar `README.md` durante este plan.

---

# 1. Objetivo general

Desarrollar, paralelizar y comparar dos algoritmos utilizando OpenMP:

- Suma de Riemann.
- Blur de imágenes.

El objetivo es demostrar con resultados reales:

- Cuándo la paralelización mejora el rendimiento.
- Cuándo el overhead puede afectar.
- Cómo cambia el tiempo al aumentar threads.
- Qué speedup se obtiene.
- Qué eficiencia se obtiene.
- Cómo influyen el scheduling, el hardware y el tamaño del problema.

---

# 2. Estructura del repositorio

```text
.
├── README.md                       # NO MODIFICAR
│
├── secuencial/
│   ├── riemann/
│   │   └── src/
│   └── blur/
│       └── src/
│
├── paralelo/
│   ├── riemann/
│   │   └── src/
│   └── blur/
│       └── src/
│
├── data/
│   ├── riemann/
│   └── blur/
│
└── docs/
    ├── contexto_datos.md
    ├── estrategia_paralelizacion.md
    ├── resultados_metricas.md
    ├── conclusiones.md
    │
    ├── resultados/
    │   ├── nery/
    │   ├── renato/
    │   └── abby/
    │
    ├── screenshots/
    │   ├── nery/
    │   ├── renato/
    │   └── abby/
    │
    └── graficas/
```

---

# 3. Responsabilidades generales

## Nery — Responsable de Suma de Riemann

Nery estará a cargo de:

- Revisar la propuesta secuencial de Riemann.
- Implementar la versión secuencial.
- Validar el resultado numérico.
- Implementar la versión paralela con OpenMP.
- Analizar `parallel for`.
- Analizar `reduction`.
- Revisar posibles race conditions.
- Probar diferentes cantidades de threads.
- Analizar scheduling.
- Documentar Riemann.
- Ejecutar sus benchmarks individuales de Riemann y Blur.

---

## Renato — Responsable de Blur

Renato estará a cargo de:

- Revisar la propuesta secuencial de Blur.
- Implementar la versión secuencial.
- Validar la imagen de salida.
- Implementar la versión paralela con OpenMP.
- Analizar qué ciclos conviene paralelizar.
- Revisar lectura y escritura de píxeles.
- Revisar bordes.
- Analizar posibles race conditions.
- Probar scheduling.
- Documentar Blur.
- Ejecutar sus benchmarks individuales de Blur y Riemann.

---

## Abby — Integración, benchmarking y optimización

Abby estará a cargo de:

- Mantener organizada la estructura.
- Verificar que todo compile.
- Verificar OpenMP.
- Integrar las soluciones de Riemann y Blur.
- Revisar consistencia entre secuencial y paralelo.
- Preparar metodología de benchmarking.
- Definir formato de resultados.
- Revisar tiempos.
- Revisar overhead.
- Revisar uso de threads.
- Revisar optimizaciones.
- Consolidar tablas.
- Generar gráficas.
- Coordinar la comparación final.
- Apoyar a Nery y Renato en optimización.
- Ejecutar sus propias pruebas individuales.

---

# 4. ETAPA 1 — Preparación del repositorio

## Objetivo
Dejar el repositorio listo para trabajar sin conflictos.

## Nery

- Clonar el repositorio.
- Crear su rama:

```text
feature/nery-riemann
```

- Revisar las carpetas de Riemann.
- Verificar que tenga acceso a:

```text
secuencial/riemann/
paralelo/riemann/
```

- Realizar al menos un commit propio.
- No modificar README.md.

## Renato

- Clonar el repositorio.
- Crear su rama:

```text
feature/renato-blur
```

- Revisar las carpetas de Blur.
- Verificar que tenga acceso a:

```text
secuencial/blur/
paralelo/blur/
```

- Realizar al menos un commit propio.
- No modificar README.md.

## Abby

- Clonar el repositorio.
- Crear su rama:

```text
feature/abby-integration
```

- Revisar toda la estructura del repositorio.
- Confirmar que existan:

```text
/secuencial
/paralelo
/docs
```

- Revisar que las carpetas estén bien organizadas.
- Verificar que no haya archivos duplicados.
- Verificar que README.md no haya sido modificado.
- Realizar al menos un commit propio.

## Resultado esperado

- [ ] Los tres tienen el repositorio.
- [ ] Los tres tienen rama.
- [ ] Los tres hicieron al menos un commit.
- [ ] La estructura está correcta.
- [ ] README.md sigue intacto.

---

# 5. ETAPA 2 — Validar compilación y OpenMP

## Objetivo
Asegurarse de que todos puedan compilar antes de implementar.

## Nery

- Verificar que pueda compilar un programa C/C++ simple.
- Verificar que pueda compilar con OpenMP.
- Anotar compilador y versión.
- Confirmar que Riemann podrá usar OpenMP.

## Renato

- Verificar compilación de C/C++.
- Verificar OpenMP.
- Confirmar que las librerías necesarias para imágenes funcionan.
- Anotar compilador y versión.

## Abby

- Definir el procedimiento de compilación común.
- Verificar cómo se compilarán las versiones:

```text
riemann_secuencial
riemann_paralelo
blur_secuencial
blur_paralelo
```

- Revisar flags de compilación.
- Verificar soporte de OpenMP en las tres computadoras.
- Documentar cualquier diferencia entre Windows, Linux o macOS.

## Resultado esperado

- [ ] Riemann puede compilar.
- [ ] Blur puede compilar.
- [ ] OpenMP funciona.
- [ ] Se conoce el compilador de cada integrante.

---

# 6. ETAPA 3 — Implementación secuencial de Riemann

## Responsable principal: Nery

## Nery

Debe:

- Definir la función a integrar.
- Definir intervalo de integración.
- Definir número de subdivisiones.
- Implementar la versión secuencial.
- Medir tiempo de ejecución.
- Mostrar el resultado numérico.
- Verificar que el cálculo sea correcto.
- Probar varios tamaños de `N`.

Tamaños iniciales sugeridos:

```text
1,000,000
10,000,000
100,000,000
```

Estos valores pueden ajustarse según rendimiento.

## Renato

- Revisar el código de Nery.
- Confirmar que la lógica sea entendible.
- Revisar posibles errores de límites.
- Verificar que el ciclo tenga el rango correcto.

## Abby

- Revisar que el tiempo se esté midiendo correctamente.
- Verificar que no se incluyan operaciones innecesarias dentro de la medición.
- Confirmar que los resultados se puedan utilizar luego como baseline.

## Resultado esperado

- [ ] Riemann secuencial funciona.
- [ ] Resultado correcto.
- [ ] Tiempo medible.
- [ ] Existe baseline secuencial.

---

# 7. ETAPA 4 — Implementación secuencial de Blur

## Responsable principal: Renato

## Renato

Debe:

- Seleccionar formato de imagen.
- Definir cómo se carga la imagen.
- Definir representación en memoria.
- Definir kernel o técnica de Blur.
- Implementar versión secuencial.
- Manejar correctamente los bordes.
- Guardar imagen de salida.
- Verificar que el Blur sea visible y correcto.
- Medir tiempo de ejecución.

## Nery

- Revisar el código secuencial de Blur.
- Verificar los ciclos.
- Revisar índices.
- Revisar límites de imagen.
- Confirmar que no haya accesos fuera de rango.

## Abby

- Verificar metodología de medición.
- Confirmar que carga y escritura de imagen no distorsionen la medición del algoritmo, si se desea medir solo el procesamiento.
- Revisar que las pruebas sean reproducibles.

## Resultado esperado

- [ ] Blur secuencial funciona.
- [ ] Imagen de salida correcta.
- [ ] Bordes manejados.
- [ ] Tiempo medible.
- [ ] Existe baseline secuencial.

---

# 8. ETAPA 5 — Selección de datos de prueba

## Nery — Riemann

Debe definir los tamaños oficiales de `N`.

La idea es tener:

- Un tamaño pequeño.
- Un tamaño mediano.
- Un tamaño grande.

Debe justificar:

- Por qué esos tamaños.
- Qué representan.
- Por qué son útiles para observar overhead y escalabilidad.

## Renato — Blur

Debe seleccionar imágenes con distintas resoluciones.

Ejemplo:

```text
Pequeña
Mediana
1920x1080
Imagen grande
```

Debe documentar:

- Resolución.
- Formato.
- Origen.
- Tamaño.
- Motivo de selección.

## Abby

Debe revisar que ambos conjuntos de pruebas sean suficientes para comparar:

- Problema pequeño.
- Problema mediano.
- Problema grande.

También debe verificar que las pruebas no sean demasiado cortas como para que el ruido del sistema domine los resultados.

## Resultado esperado

- [ ] Datos oficiales de Riemann definidos.
- [ ] Imágenes oficiales de Blur definidas.
- [ ] Justificación escrita.

---

# 9. ETAPA 6 — Paralelización de Riemann

## Responsable principal: Nery

## Nery

Debe analizar e implementar OpenMP.

Evaluar:

```cpp
#pragma omp parallel for
```

y especialmente:

```cpp
reduction(+:sum)
```

Debe explicar:

- Qué ciclo se paralelizó.
- Por qué puede dividirse.
- Qué variable podría producir race condition.
- Por qué `reduction` resuelve el problema.
- Qué variables son privadas.
- Qué variables son compartidas.
- Qué scheduling se utilizó.

## Renato

- Revisar el código paralelo de Nery.
- Verificar que el resultado sea correcto.
- Buscar posibles race conditions.
- Comparar visualmente la estructura secuencial y paralela.

## Abby

- Revisar overhead.
- Revisar cantidad de regiones paralelas.
- Confirmar que los threads se utilicen de forma eficiente.
- Revisar si la paralelización está en el nivel correcto.
- Apoyar con optimizaciones.

## Resultado esperado

- [ ] Riemann paralelo compila.
- [ ] OpenMP funciona.
- [ ] Resultado correcto.
- [ ] Race condition controlada.
- [ ] Estrategia documentada.

---

# 10. ETAPA 7 — Paralelización de Blur

## Responsable principal: Renato

## Renato

Debe:

- Identificar el ciclo más adecuado para paralelizar.
- Evaluar paralelización por filas o píxeles.
- Implementar OpenMP.
- Garantizar que cada thread escriba correctamente.
- Mantener lectura segura de la imagen original.
- Revisar bordes.
- Revisar scheduling.
- Comparar resultado con secuencial.

## Nery

- Revisar implementación.
- Verificar índices.
- Revisar si hay escrituras compartidas.
- Validar que el resultado paralelo coincida con el secuencial.

## Abby

- Revisar distribución del trabajo.
- Revisar cache locality.
- Revisar overhead.
- Evaluar si `collapse` tendría sentido.
- Revisar scheduling.
- Apoyar la optimización.

## Resultado esperado

- [ ] Blur paralelo compila.
- [ ] Resultado correcto.
- [ ] No hay corrupción visual.
- [ ] OpenMP funciona.
- [ ] Estrategia documentada.

---

# 11. ETAPA 8 — Validación de resultados

## Nery

### Riemann
- Comparar resultado secuencial vs paralelo.
- Medir diferencia numérica.
- Confirmar que sea razonable.

### Blur
- Apoyar revisión de resultado.
- Verificar que la salida tenga las dimensiones correctas.

## Renato

### Blur
- Comparar imagen secuencial vs paralela.
- Validar píxeles o checksum si se implementa.
- Revisar bordes.

### Riemann
- Revisar que ambas versiones produzcan resultados equivalentes.

## Abby

- Crear criterios de validación comunes.
- Verificar que nadie continúe con benchmarks si el algoritmo paralelo es incorrecto.
- Confirmar que las versiones finales sean comparables.

## Regla

> Una solución paralela más rápida pero incorrecta no cuenta como una mejora.

---

# 12. ETAPA 9 — Diseñar benchmarking oficial

## Responsable principal: Abby

## Abby

Debe definir el protocolo oficial de medición.

Configuraciones iniciales:

```text
Secuencial
1 thread
2 threads
4 threads
8 threads
```

Si el hardware lo permite:

```text
12 threads
16 threads
```

Debe definir:

- Cantidad de repeticiones.
- Formato de resultados.
- Qué se mide.
- Qué no se mide.
- Cómo se obtiene el promedio.
- Cómo se calculan speedup y eficiencia.

Recomendación:

```text
5 repeticiones por configuración
```

## Nery

- Revisar que el benchmark sea adecuado para Riemann.
- Confirmar tamaños de `N`.
- Verificar que los tiempos sean suficientemente grandes.

## Renato

- Revisar que el benchmark sea adecuado para Blur.
- Confirmar resoluciones.
- Verificar que el procesamiento se mida de forma consistente.

## Resultado esperado

- [ ] Existe un protocolo único.
- [ ] Los tres usarán las mismas configuraciones.
- [ ] Los resultados serán comparables.

---

# 13. ETAPA 10 — Registrar hardware

## Cada integrante

Debe registrar:

```text
Nombre:
Sistema operativo:
Procesador:
Núcleos físicos:
Núcleos lógicos:
RAM:
Compilador:
Versión:
Soporte OpenMP:
```

## Nery

Guardar en:

```text
docs/resultados/nery/
```

## Renato

Guardar en:

```text
docs/resultados/renato/
```

## Abby

Guardar en:

```text
docs/resultados/abby/
```

## Abby además

- Consolidar la información de hardware.
- Revisar diferencias importantes entre las tres máquinas.

---

# 14. ETAPA 11 — Benchmarks individuales de Nery

## Nery

Debe ejecutar ambos algoritmos en su propia computadora.

### Riemann

Para cada `N`:

```text
Secuencial
1 thread
2 threads
4 threads
8 threads
```

Cada configuración:

```text
5 repeticiones
```

### Blur

Para cada imagen:

```text
Secuencial
1 thread
2 threads
4 threads
8 threads
```

También 5 repeticiones.

Guardar:

```text
docs/resultados/nery/
docs/screenshots/nery/
```

## Renato

- Revisar que las pruebas de Blur de Nery sean válidas.

## Abby

- Verificar formato.
- Verificar promedios.
- Revisar que Nery tenga todas sus evidencias.

---

# 15. ETAPA 12 — Benchmarks individuales de Renato

## Renato

Debe ejecutar ambos algoritmos.

### Blur

Ejecutar todas las imágenes y configuraciones.

### Riemann

Ejecutar todos los valores de `N`.

Guardar:

```text
docs/resultados/renato/
docs/screenshots/renato/
```

## Nery

- Revisar que los resultados de Riemann de Renato tengan sentido.

## Abby

- Verificar formato.
- Verificar promedios.
- Confirmar screenshots.

---

# 16. ETAPA 13 — Benchmarks individuales de Abby

## Abby

Debe ejecutar ambos algoritmos en su computadora.

### Riemann
- Secuencial.
- 1 thread.
- 2 threads.
- 4 threads.
- 8 threads.

### Blur
- Secuencial.
- 1 thread.
- 2 threads.
- 4 threads.
- 8 threads.

Guardar:

```text
docs/resultados/abby/
docs/screenshots/abby/
```

## Nery

- Revisar resultados de Riemann de Abby.

## Renato

- Revisar resultados de Blur de Abby.

---

# 17. ETAPA 14 — Speedup y eficiencia

## Fórmulas

### Speedup

```text
Speedup = Tiempo secuencial / Tiempo paralelo
```

### Eficiencia

```text
Eficiencia = Speedup / Número de threads
```

Porcentaje:

```text
Eficiencia (%) = (Speedup / Número de threads) × 100
```

## Nery

- Calcular speedup y eficiencia de sus resultados.
- Revisar especialmente Riemann.

## Renato

- Calcular speedup y eficiencia de sus resultados.
- Revisar especialmente Blur.

## Abby

- Calcular sus propias métricas.
- Revisar los cálculos de todos.
- Consolidar los resultados en una tabla común.
- Detectar valores extraños o inconsistentes.

---

# 18. ETAPA 15 — Scheduling

## Nery — Riemann

Probar, cuando tenga sentido:

```text
schedule(static)
schedule(dynamic)
```

Analizar:

- Uniformidad del trabajo.
- Overhead.
- Diferencias de tiempo.

## Renato — Blur

Probar:

```text
schedule(static)
schedule(dynamic)
```

si aplica.

Analizar:

- Distribución por filas/píxeles.
- Costo similar por iteración.
- Efecto sobre tiempo.

## Abby

- Coordinar comparación.
- Revisar si realmente vale la pena usar `dynamic`.
- Evitar conclusiones sin datos.
- Seleccionar con el equipo la configuración final.

---

# 19. ETAPA 16 — Optimización

## Responsable principal: Abby

## Abby

Debe revisar ambos algoritmos.

### Riemann

Buscar:

- Overhead innecesario.
- Creación excesiva de regiones paralelas.
- Reducciones.
- Uso de threads.
- Scheduling.
- Escalabilidad.

### Blur

Buscar:

- Accesos innecesarios a memoria.
- Cache locality.
- Operaciones repetidas.
- Distribución de filas.
- Scheduling.
- Posible false sharing.
- Overhead.

## Nery

- Aplicar mejoras a Riemann.
- Volver a validar resultado.
- Volver a medir si se modifica el código.

## Renato

- Aplicar mejoras a Blur.
- Volver a validar la imagen.
- Volver a medir.

## Resultado esperado

- [ ] Versiones finales estables.
- [ ] Optimizaciones justificadas.
- [ ] Sin romper exactitud.

---

# 20. ETAPA 17 — Gráficas

## Responsable principal: Abby

## Abby

Debe generar:

### Para Riemann

```text
riemann_tiempo_vs_threads.png
riemann_speedup.png
riemann_eficiencia.png
```

### Para Blur

```text
blur_tiempo_vs_threads.png
blur_speedup.png
blur_eficiencia.png
```

## Nery

- Revisar gráficas de Riemann.
- Confirmar que representan correctamente sus resultados y los datos consolidados.

## Renato

- Revisar gráficas de Blur.
- Confirmar etiquetas, resoluciones y resultados.

## Abby

- Verificar títulos.
- Ejes.
- Unidades.
- Leyendas.
- Comparabilidad.

---

# 21. ETAPA 18 — Contexto y datos

Archivo:

```text
docs/contexto_datos.md
```

## Nery

Escribir la sección de Riemann:

- Qué es.
- Qué calcula.
- Solución secuencial.
- Función.
- Intervalo.
- Número de subdivisiones.
- Datos de prueba.
- Justificación.
- Uso de memoria.

## Renato

Escribir la sección de Blur:

- Qué es.
- Cómo funciona.
- Solución secuencial.
- Kernel.
- Imagen.
- Resoluciones.
- Datos de prueba.
- Justificación.
- Uso de memoria.

## Abby

- Integrar ambas secciones.
- Revisar que tengan estructura similar.
- Corregir inconsistencias.
- Confirmar que los datos usados coincidan con los benchmarks reales.

---

# 22. ETAPA 19 — Estrategia de paralelización

Archivo:

```text
docs/estrategia_paralelizacion.md
```

## Nery

Documentar Riemann:

- Ciclo paralelizado.
- `parallel for`.
- `reduction`.
- Variables privadas.
- Variables compartidas.
- Race conditions.
- Scheduling.
- Overhead.

## Renato

Documentar Blur:

- Ciclos paralelizados.
- Distribución del trabajo.
- Lectura/escritura.
- Race conditions.
- Scheduling.
- Bordes.
- Decisiones de OpenMP.

## Abby

- Revisar ambas secciones.
- Confirmar que cada directiva esté justificada.
- Agregar comparación general si aplica.
- Verificar que no sea solo una copia del código.

---

# 23. ETAPA 20 — Resultados y métricas

Archivo:

```text
docs/resultados_metricas.md
```

## Nery

Escribir:

```text
## Nery
### Hardware
### Riemann
### Blur
### Speedup
### Eficiencia
### Interpretación
```

## Renato

Escribir:

```text
## Renato
### Hardware
### Riemann
### Blur
### Speedup
### Eficiencia
### Interpretación
```

## Abby

Escribir:

```text
## Abby
### Hardware
### Riemann
### Blur
### Speedup
### Eficiencia
### Interpretación
```

Además Abby debe crear:

```text
## Comparación general
```

Comparando:

- Diferencias entre computadoras.
- Mejor cantidad de threads.
- Escalabilidad.
- Overhead.
- Diferencias entre Blur y Riemann.

---

# 24. ETAPA 21 — Conclusiones

Archivo:

```text
docs/conclusiones.md
```

## Nery

Aportar conclusiones de Riemann:

- ¿Mejoró?
- ¿Cuánto?
- ¿Con cuántos threads?
- ¿Dónde apareció overhead?
- ¿El tamaño de `N` influyó?

## Renato

Aportar conclusiones de Blur:

- ¿Mejoró?
- ¿Con qué resolución?
- ¿Cuántos threads fueron mejores?
- ¿Qué limitaciones aparecieron?
- ¿Cómo influyó memoria?

## Abby

- Integrar conclusiones.
- Comparar ambos algoritmos.
- Explicar cuál escaló mejor.
- Explicar por qué más threads no necesariamente significa más velocidad.
- Revisar que todo esté respaldado por datos.

---

# 25. ETAPA 22 — Evidencias

## Nery

Guardar sus capturas en:

```text
docs/screenshots/nery/
```

## Renato

Guardar en:

```text
docs/screenshots/renato/
```

## Abby

Guardar en:

```text
docs/screenshots/abby/
```

## Abby además

Debe verificar que cada integrante tenga evidencia suficiente de:

- Riemann.
- Blur.
- Diferentes threads.
- Tiempos.

---

# 26. ETAPA 23 — Revisión cruzada

## Nery revisa

- Blur de Renato.
- Documentación de Blur.
- Resultados de Riemann de los demás.

## Renato revisa

- Riemann de Nery.
- Documentación de Riemann.
- Resultados de Blur de los demás.

## Abby revisa

- Integración completa.
- Compilación.
- Resultados.
- Benchmarking.
- Gráficas.
- Documentación.
- Consistencia de nombres y rutas.

---

# 27. ETAPA 24 — Validación final

## Nery

- Compilar Riemann secuencial.
- Compilar Riemann paralelo.
- Ejecutar pruebas finales.
- Confirmar exactitud.
- Confirmar documentación de Riemann.

## Renato

- Compilar Blur secuencial.
- Compilar Blur paralelo.
- Ejecutar pruebas finales.
- Confirmar imágenes.
- Confirmar documentación de Blur.

## Abby

Ejecutar revisión final:

- Compilación completa.
- OpenMP activo.
- Carpetas correctas.
- Resultados presentes.
- Screenshots presentes.
- Gráficas presentes.
- Speedup calculado.
- Eficiencia calculada.
- Cada integrante tiene participación.
- README.md no fue modificado.
- `git status` limpio o con cambios conocidos.
- No hay archivos innecesarios.
- No hay resultados inventados.

---

# 28. Estrategia Git

## Ramas principales

```text
feature/nery-riemann
feature/renato-blur
feature/abby-integration
```

## Commits sugeridos para Nery

```text
feat: add sequential riemann implementation
feat: add OpenMP riemann implementation
test: validate riemann results
docs: document riemann strategy
```

## Commits sugeridos para Renato

```text
feat: add sequential blur implementation
feat: add OpenMP blur implementation
test: validate blur output
docs: document blur strategy
```

## Commits sugeridos para Abby

```text
chore: organize integration workflow
feat: add benchmark support
perf: review parallel performance
docs: consolidate benchmark results
docs: add performance graphs
```

---

# 29. Orden recomendado de integración

1. Estructura base.
2. Riemann secuencial.
3. Blur secuencial.
4. Validaciones.
5. Riemann paralelo.
6. Blur paralelo.
7. Validación paralelo.
8. Benchmarking.
9. Optimización.
10. Benchmarks oficiales.
11. Speedup y eficiencia.
12. Gráficas.
13. Documentación.
14. Evidencias.
15. Revisión cruzada.
16. Validación final.

---

# 30. Checklist de Nery

## Suma de Riemann

- [ ] Secuencial implementado.
- [ ] Resultado validado.
- [ ] Datos de prueba definidos.
- [ ] Paralelo implementado.
- [ ] `reduction` evaluado.
- [ ] Race conditions analizadas.
- [ ] Scheduling probado.
- [ ] Optimización aplicada.
- [ ] Documentación escrita.

## Parte individual

- [ ] Benchmarks de Riemann.
- [ ] Benchmarks de Blur.
- [ ] Speedup.
- [ ] Eficiencia.
- [ ] Hardware documentado.
- [ ] Screenshots.
- [ ] Al menos un commit.

---

# 31. Checklist de Renato

## Blur

- [ ] Secuencial implementado.
- [ ] Imagen validada.
- [ ] Datos de prueba definidos.
- [ ] Paralelo implementado.
- [ ] Race conditions analizadas.
- [ ] Scheduling probado.
- [ ] Bordes revisados.
- [ ] Optimización aplicada.
- [ ] Documentación escrita.

## Parte individual

- [ ] Benchmarks de Blur.
- [ ] Benchmarks de Riemann.
- [ ] Speedup.
- [ ] Eficiencia.
- [ ] Hardware documentado.
- [ ] Screenshots.
- [ ] Al menos un commit.

---

# 32. Checklist de Abby

## Integración, benchmarking y optimización

- [ ] Estructura revisada.
- [ ] Compilación revisada.
- [ ] OpenMP revisado.
- [ ] Protocolo de benchmarks definido.
- [ ] Resultados consolidados.
- [ ] Cálculos revisados.
- [ ] Optimización de Riemann revisada.
- [ ] Optimización de Blur revisada.
- [ ] Gráficas generadas.
- [ ] Documentación integrada.
- [ ] Evidencias revisadas.
- [ ] Validación final realizada.

## Parte individual

- [ ] Benchmarks de Riemann.
- [ ] Benchmarks de Blur.
- [ ] Speedup.
- [ ] Eficiencia.
- [ ] Hardware documentado.
- [ ] Screenshots.
- [ ] Al menos un commit.

---

# 33. Matriz rápida de responsables

| Etapa | Nery | Renato | Abby |
|---|---|---|---|
| Preparación | Rama Riemann | Rama Blur | Integración |
| Compilación | Revisar Riemann | Revisar Blur | Estandarizar |
| Secuencial Riemann | **Responsable** | Revisión | Medición |
| Secuencial Blur | Revisión | **Responsable** | Medición |
| Datos Riemann | **Responsable** | Apoyo | Revisión |
| Datos Blur | Apoyo | **Responsable** | Revisión |
| Paralelo Riemann | **Responsable** | Revisión | Optimización |
| Paralelo Blur | Revisión | **Responsable** | Optimización |
| Validación | Riemann | Blur | Coordinación |
| Benchmarking | Ejecutar | Ejecutar | **Responsable** |
| Hardware | Registrar | Registrar | Consolidar |
| Speedup | Calcular | Calcular | Revisar |
| Eficiencia | Calcular | Calcular | Revisar |
| Scheduling Riemann | **Responsable** | Apoyo | Analizar |
| Scheduling Blur | Apoyo | **Responsable** | Analizar |
| Optimización | Aplicar Riemann | Aplicar Blur | **Responsable** |
| Gráficas | Revisar Riemann | Revisar Blur | **Responsable** |
| Contexto y datos | Riemann | Blur | Integrar |
| Estrategia OpenMP | Riemann | Blur | Integrar |
| Resultados | Parte individual | Parte individual | Consolidar |
| Conclusiones | Riemann | Blur | Integrar |
| Evidencias | Propias | Propias | Revisar todas |
| Revisión final | Riemann | Blur | **Responsable** |

---

# 34. Flujo completo

```text
Preparar repositorio
        ↓
Compilar y validar OpenMP
        ↓
Nery → Riemann secuencial
Renato → Blur secuencial
Abby → integración y medición
        ↓
Validar ambas versiones
        ↓
Nery → Riemann paralelo
Renato → Blur paralelo
Abby → revisión de OpenMP y optimización
        ↓
Validar resultados
        ↓
Abby → protocolo de benchmarking
        ↓
Nery ejecuta ambos algoritmos
Renato ejecuta ambos algoritmos
Abby ejecuta ambos algoritmos
        ↓
Calcular speedup y eficiencia
        ↓
Probar scheduling
        ↓
Abby coordina optimización
        ↓
Repetir benchmarks oficiales
        ↓
Generar gráficas
        ↓
Completar documentación
        ↓
Revisión cruzada
        ↓
Validación final
        ↓
Entrega
```

---

# 35. Criterio de terminado

El proyecto estará terminado cuando el equipo pueda demostrar claramente:

> “Nery desarrolló y justificó la paralelización de Suma de Riemann, Renato desarrolló y justificó la paralelización de Blur, Abby coordinó la integración, benchmarking y optimización, y los tres realizaron mediciones individuales que permiten comparar tiempos, speedup y eficiencia en hardware diferente.”

El objetivo final no es demostrar que OpenMP siempre sea más rápido. El objetivo es demostrar con datos cuándo la paralelización funciona, cuándo aparece overhead y cómo influyen el tamaño del problema, el número de threads, el scheduling y el hardware.
