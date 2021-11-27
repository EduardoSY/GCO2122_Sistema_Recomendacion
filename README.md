# GCO: Sistemas de recomendación

- **Autor:** Eduardo Da Silva Yanes
- **Asignatura:** Gestión del conocimiento en las organizaciones
- **Centro:** ESIT - Universidad de La Laguna

***

### Objetivo de la práctica:

El objetivo de esta práctica es implementar un sistema de recomendación siguiendo el método de filtrado colaborativo.

### Descripción de la implementación:

El código implementado para la realización de esta práctica ha sido escrito en Python. Al tratarse de mi primer acercamiento al lenguaje es muy probable que hayan formas mucho más rápida y optimas de realizar las funciones.



**IMPLEMENTACIÓN**

1. Lectura e inicialización de las matrices.

Lo primero que debemos hacer es leer la matriz y estructurarla de la manera correcta para ser leida y manipulada. Para realizar esto leemos línea a línea en el documento, la procesamos y la guardamos en un vector. Este vector lo insertamos a su vez en otro vector, formando así una matriz.

Una vez hecho esto creamos la matriz de similitud. Esta será cuadrada y cuyas dimensiones coinciden, como es lógico, con el número de usuarios. Puesto que aún podemos calcular los valores lo que haremos será rellenarla de valores vacios.

2. Implementación de métricas

Con las siguientes funciones podremos calcular la similitud entre un usuario a y un usuario b. En nuestro caso tenemos 3 alternativas.

  1. Correlación de Pearson

  ![Cap_Pearson](./img/pearson_cv.png)

  2. Distancia coseno

  ![Cap_Coseno](./img/pearson_cv.png)

  3. Distancia euclídea

  ![Cap_euclidea](./img/pearson_cv.png)

La implementación consiste simplemente en aplicar la fórmula matemática mostrada en las diapositivas del campus virtual. Es por ello que no considero necesario entrar en mucho detalle. 
### Ejemplo de uso

Para usar el programa debemos ejecutar algo similar a lo siguiente: ```python GCO.py "fichero.txt" pearson 5 simple```

- "fichero.txt" es el fichero donde se encuentra la matriz.
- person es el método usado para calcular la similitud. Las opciones son: pearson, euclidea, coseno
- 5 es el número de vecinos a considerar
- simple es el método de prediccion. Las opciones son: simple y media.

A continuación se muestra un ejemplo de uso respecto al software desarrollado.

```
$python GCO.py matrices_para_probar/matrix_test.txt pearson 3 simple

1. Metrica empleada: pearson
2. Metodo de prediccion: simple
3. Numero de vecinos: 3
---------------------
MATRIZ DE SIMILITUDES
[0] ->  1.0000          0.8528          0.7071          0.0000          -0.7921
[1] ->  0.8528          1.0000          0.4677          0.4900          -0.9001
[2] ->  0.7071          0.4677          1.0000          -0.1612         -0.4666
[3] ->  0.0000          0.4900          -0.1612         1.0000          -0.6415
[4] ->  -0.7921         -0.9001         -0.4666         -0.6415         1.0000
----------------------------------
Vecinos utilizados para calcular Usuario 0 -> Item 4
[(1, 0.8528028654224417), (2, 0.7071067811865475), (4, -0.7921180343813393)]
Resultado prediccion: 2.2542
--- MATRIZ CON LAS PREDICCIONES ---
[0] ->  5.00            3.00            4.00            4.00            2.25
[1] ->  3.00            1.00            2.00            3.00            3.00
[2] ->  4.00            3.00            4.00            3.00            5.00
[3] ->  3.00            3.00            1.00            5.00            4.00
[4] ->  1.00            5.00            5.00            2.00            1.00
```

**ATENCIÓN**: Al utilizar matrices de mayor tamaño es posible que la visualización en la terminal no se la correcta. En esos casos recomiendo redirigir la salida a un fichero de texto y visualizar desde ahí los resultados.

``` python GCO.py "fichero.txt" pearson 5 simple > fichero_salida.txt```

En [este enlace](https://github.com/EduardoSY/GCO2122_Sistema_Recomendacion/tree/main/resultados_matrices) tenemos diversos ficheros de salida de pruebas ejecutadas con el codigo implementado.
