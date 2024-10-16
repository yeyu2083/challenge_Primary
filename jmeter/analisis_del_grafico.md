# Análisis de los tres escenarios:

## Escenario 1: Prueba de Estrés (línea azul)
- El tiempo de respuesta comienza alrededor de los 2 milisegundos y aumenta de manera constante hasta alcanzar picos cercanos a 3 milisegundos antes de estabilizarse nuevamente.
- Este comportamiento indica que, bajo condiciones de estrés, el sistema tiende a experimentar un aumento en los tiempos de respuesta debido a la saturación.
- Después de este aumento, parece haber una estabilización en los tiempos de respuesta con fluctuaciones menores.

## Escenario 2: Prueba de Carga (línea roja)
- En la prueba de carga, el tiempo de respuesta sigue una tendencia similar a la de la prueba de estrés al principio, pero se estabiliza más rápidamente y a un nivel más bajo.
- Aquí los tiempos de respuesta se mantienen relativamente constantes en comparación con la prueba de estrés, lo que indica que el sistema maneja bien cargas moderadas sin mayores problemas.

## Escenario 3: Prueba de Volumen (línea verde)
- La prueba de volumen tiene los tiempos de respuesta más bajos en general. El tiempo de respuesta se mantiene cercano a los 2 milisegundos, con muy pocas fluctuaciones.
- El pequeño salto que se observa en el gráfico podría deberse a la inicialización del sistema bajo la carga de gran cantidad de datos, pero una vez que el sistema estabiliza, los tiempos de respuesta se mantienen estables.

## Conclusión:
- **Prueba de Estrés**: El sistema experimenta un aumento significativo en los tiempos de respuesta cuando se somete a estrés, lo que sugiere que, a medida que la demanda aumenta más allá de un umbral, el rendimiento se degrada.
- **Prueba de Carga**: El sistema maneja bien las cargas moderadas, con tiempos de respuesta que permanecen constantes sin grandes fluctuaciones.
- **Prueba de Volumen**: A pesar de manejar grandes cantidades de datos, el sistema parece ser capaz de procesar rápidamente y de manera consistente, lo que es un buen indicador de rendimiento bajo volumen.
