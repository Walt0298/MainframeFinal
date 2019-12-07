# Ejercicios Repaso para Examen Final

## Teoría

1. **¿Cuál es la finalidad de una normalización de datos?**
- Normalizar datos es una técnica que se aplica a un conjunto de datos para ajustar los valores en diferentes escalas respecto a una escala común. 
- El objetivo principal de esta técnica uniformizar y ajustar los datos a una escala específica para obtener datos más limpios, rápidos y más útiles para la analítica.
2. **Indique 5 ejemplos de la aplicación de KNN**
- **Detección de cáncer de mama**. Se entrena al modelo con imágenes muestra de cáncer de mama para que luego se le ingrese una nueva imagen de prueba yel modelo determine si existe cáncer o no.
- **Sistema de recomendación de Videos**. Se toma como datos de entrenamiento las preferencias de videos de las personas agrupandolos en segmentos para que luego se realicen sugerencias de video relacionados que podrían gustarle
- **Análisis de sentimientos**. Se entrena al modelo con las opiniones de personas sobre algo en específico para clasificarlos según positividad o negatividad
- **Score crediticio**. Se entrena al modelo con los datos de clientes de bancos sobre sus transacciones y deudas para clasificarlos para que luego el modelo pueda determinar si se le da crédito a un cliente
- **Segmentación del mercado**. Entrenar al modelo con datos de clientes de una organización para poder conocer que tipos de clientes cuenta mediante la clasificación de los mismos hecho por el modelo
3. **Indique 5 ejemplos de la aplicación de KMeans**
- Clasificación de patrones de datos de _gráficas de velas japonesas_ sobre la tendencia del mercado
- Determinación del nivel de robustez operativo de un software de trading
- Clasificación de las acciones de empresas según sus características(retorno histórico y volatilidad)
- Segmentación de clientes mediante preferencias de productos o servicio
- Clasificación de jugadores que utilizan y no utilizan programas facilitadores sobre un juego mediante el patrón de juego
4. **¿Describa 2 Ejemplos donde se aplique una Regla de Asociación?**
- Conocer los patrones de adquisición de productos o servicios de los clientes
- Conocer los patrones causantes de adquisición de adquisición de productos o servicios de los clientes
5. **¿Cuáles son las diferencias entre una Regresión Lineal y Polinomial?**
- Difieren en el grado del polinomio, una regresión lineal está limitada a un polinomio de grado 1, mientras que una regresión polinomial está sujeta a polinomios de grado 2, 3, 4, ..., n
6. **¿En qué casos se utiliza como métrica de similaridad una distancia Jackard y coseno?**
- Jaccard: Conocer que tantos elementos comparten dos vectores, que tan similares son
- Coseno: Conocer la proximidad entre dos vector según el ángulo del vector de visión
7. **¿Cuál es la finalidad de una Matriz de Confusión?**
- Es una herramienta que permite la visualización del desempeño de un algoritmo que se emplea en aprendizaje supervisado. Cada columna de la matriz representa el número de predicciones de cada clase, mientras que cada fila representa a las instancias en la clase real. Uno de los beneficios de las matrices de confusión es que facilitan ver si el sistema está confundiendo dos clases.
8. **¿Dentro del Aprendizaje Automático, a que se denomina fitting?**
- Un ajuste estadístico o fitting se refiere a qué tan bien aproxima el algoritmo una función objetivo.
9. **¿En qué caso aplicaría SVM?**
- Cuando se tenga un problema binario y se quiera clasificar(dividir) un conjunto de datos lo más preciso posible
10. **¿A qué se denomina Falso Positivo y Falso Negativo?**
- Falso positivo.Sucede cuando el modelo determina que SI existe problema cuando en realidad NO existe
- Falso negativo. Sucede cuando el modelo determina que NO existe problema cuando en realidad SI existe
11. **¿Para qué se usa una matriz de correlación?**
- Para conocer el nivel de correlación entre todas las variables cuantitativas de un sistema

## Implementación

3. [Caso de Estudio: Mesa Redonda](mesa_redonda/mesa_redonda.md)