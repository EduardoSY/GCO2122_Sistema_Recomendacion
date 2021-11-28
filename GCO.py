# Autor: Eduardo Da Silva Yanes

#MickeyHerramientas:
#Con type(variable) puedo ver el tipo de la variable.

import argparse
import math
from copy import deepcopy

# ----- CALCULO DE METRICAS -----

# -> Pearson
def coef_corr_pearson(usuario_u, usuario_v):
    vector_usuario_u, vector_usuario_v = valores_comunes(usuario_u, usuario_v)
    media_user_u = media(vector_usuario_u)
    media_user_v = media(vector_usuario_v)
    
    #print "Usuario u media " + str(media_user_u)
    #print "Usuario v media " + str(media_user_v)
    
    numerador = 0
    sum_raiz_izq = 0
    sum_raiz_der = 0
    for i in range(len(matriz[usuario_u])):
        if ((matriz[usuario_u][i] != '-') and (matriz[usuario_v][i] != '-')): 
            numerador += ((matriz[usuario_u][i] - media_user_u) * (matriz[usuario_v][i] - media_user_v))
            sum_raiz_izq += (matriz[usuario_u][i] - media_user_u) ** 2
            sum_raiz_der += (matriz[usuario_v][i] - media_user_v) ** 2
    
    resultado = (numerador / (math.sqrt(sum_raiz_izq) * math.sqrt(sum_raiz_der)))
    return resultado

# -> Distancia euclidea
def dist_euclidea(usuario_u, usuario_v):
    resultado = 0
    #contador = 0
    for i in range(len(matriz[usuario_u])):
        if ((matriz[usuario_u][i] != '-') and (matriz[usuario_v][i] != '-')):  
            resultado += ((matriz[usuario_u][i] - matriz[usuario_v][i])**2)
            #contador += 1
    resultado = math.sqrt(resultado)
    #resultado = resultado / float(contador)
    return resultado

# -> Distancia coseno
def dist_cos(usuario_u, usuario_v):
    numerador = 0
    sum_raiz_izq = 0
    sum_raiz_der = 0
    
    for i in range(len(matriz[usuario_u])):
        if ((matriz[usuario_u][i] != '-') and (matriz[usuario_v][i] != '-')): 
            # print "---------------------"
            # print matriz[usuario_u][i]
            # print matriz[usuario_v][i]
            numerador += matriz[usuario_u][i] * matriz[usuario_v][i]
            sum_raiz_izq += (matriz[usuario_u][i]) ** 2
            sum_raiz_der += (matriz[usuario_v][i]) ** 2

    resultado = (numerador / (math.sqrt(sum_raiz_izq) * math.sqrt(sum_raiz_der)))
    return resultado

# -----------------------------------

# ----- CALCULO DE PREDICCIONES -----

# -> Calcular las similitudes
def calculo_sim(metodo):
    if (metodo == "pearson"):
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                matriz_similitudes[i][j] = coef_corr_pearson(i, j)
    elif (metodo == "coseno"): 
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                matriz_similitudes[i][j] = dist_cos(i, j)
        print "Usando Coseno"
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                matriz_similitudes[i][j] = dist_euclidea(i, j)
        print "Usando euclidea"

# -> Prediccion simple
def prediccion_simple(pos_predecir, k_vecinos):
    numerador = 0
    denominador = 0
    for i in k_vecinos:
        #print (pos_predecir)
        numerador += (i[1] * matriz[i[0]][pos_predecir])

        
        denominador += abs(i[1])
    resultado = numerador / float(denominador)
    resultado_formato = "{:.4f}".format(resultado)
    resultado = float(resultado_formato)
    
    if resultado < 0:
        resultado = 0
    elif resultado > 5:
        resultado = 5

    return resultado

# -> Prediccion usando diferencia con la media
def prediccion_dif_media(usuario, pos_predecir, k_vecinos):
    media_usuario = media(matriz[usuario])
    #print "Media usuario: " + str(media_usuario)
    medias = []
    for i in k_vecinos:
        medias.append(media(matriz[i[0]]))
    #print medias

    numerador = 0
    denominador = 0
    for i in k_vecinos:
        #print (pos_predecir)
        numerador += (i[1] * (matriz[i[0]][pos_predecir] - media(matriz[i[0]])))
        denominador += abs(i[1])

    resultado = media_usuario + (numerador / float(denominador))
    
    if resultado < 0:
        resultado = 0
    elif resultado > 5:
        resultado = 5

    return resultado

    return resultado

#------------------------------------

#------- FUNCIONES AUXILIARES -------

# -> Calcular la media
def media(dataset):
    datos = []

    for i in dataset:
        if i != '-':
            datos.append(i)
    
    return sum(datos) / float(len(datos))

# -> Calcular item comunes que los usuarios u y v han votado
def valores_comunes(usuario_u, usuario_v):
    vector_usuario_u = []
    vector_usuario_v = []
    for i in range(len(matriz[usuario_u])):
      if(matriz[usuario_u][i] != '-' and matriz[usuario_v][i] != '-'):
          vector_usuario_u.append(matriz[usuario_u][i])
          vector_usuario_v.append(matriz[usuario_v][i])
    return vector_usuario_u, vector_usuario_v


# -> Calcular los vecinos para hacer las predicciones
def calcular_vecinos(metrica, neighbors, usuario_x, pos_calcular):
    k_vecinos = []
    fila_usuario_ordenar = deepcopy(matriz_similitudes[usuario_x])
    if ((metrica == 'pearson') or (metrica == 'coseno')):
        fila_usuario_ordenar.sort(reverse=True) #Ya esta modificado
    else:
        fila_usuario_ordenar.sort(reverse=False)
    #print "Fila Usuario limpia"
    
    fila_usuario_limpia = deepcopy(matriz_similitudes[usuario_x])
    #print fila_usuario_limpia
    fila_usuario_limpia2 = deepcopy(fila_usuario_limpia)
    vecinos_coincidentes = []
    
    
    for elemento in fila_usuario_ordenar:
        
        usuario = fila_usuario_limpia2.index(elemento)
        fila_usuario_limpia2[usuario] = 0
        #print usuario #Obtengo el usuario
        if(matriz[usuario][pos_calcular] != '-'): #Analiza si ha votado el item
            vecinos_coincidentes.append(usuario)

    cantidad_vecinos = vecinos_coincidentes[0:neighbors] #Vecinos que se van a usar

    for i in cantidad_vecinos:
        valor_similitud = fila_usuario_limpia[i]
        k_vecinos.append((i, valor_similitud))
    print "Vecinos utilizados para calcular Usuario " + str(usuario_x) + " -> Item " + str(pos_calcular)
    print k_vecinos 
    return k_vecinos #Devuelve un par (usuario, similitud)

# -> --- MOSTRAR MATRICES ---
def show_matriz(matrix):
    for i in range(len(matrix)):
        aux_fila = "[" + str(i) + "] ->  "
        for j in range(len(matrix[i])):
            aux_fila += "{:.2f}".format(matrix[i][j])
            aux_fila += "\t\t"
        print aux_fila

def show_matriz_similitud():
  print "---------------------"
  print "MATRIZ DE SIMILITUDES"
  for i in range(len(matriz_similitudes)):
        aux_fila = "[" + str(i) + "] ->  "
        for j in range(len(matriz_similitudes[i])):
           aux_fila += "{:.4f}".format(matriz_similitudes[i][j])
           aux_fila += "\t\t"
        print aux_fila


# [---][---] FUNCION PRINCIPAL DE GESTION [---][---]
def main(metrica, prediccion, vecinos):
    print ("1. Metrica empleada: " + metrica)
    print ("2. Metodo de prediccion: " + prediccion)
    print ("3. Numero de vecinos: " + str(vecinos))
    calculo_sim(metrica)
    show_matriz_similitud()

    matriz_final = deepcopy(matriz)

    for i in usuarios_predecir: #Usuarios de los que tenemos que predecir
        for j in range(len(matriz[i])):  #Recorremos buscando posiciones a predecir
            if (matriz_final[i][j] == '-'): #Encontrada posicion a predecir
                print "----------------------------------"
                k = calcular_vecinos(metrica, vecinos, i, j)
                if(prediccion == "simple"):
                    pred  = prediccion_simple(j, k)
                    
                    print "Resultado prediccion: " + str(pred)
                    matriz_final[i][j] = pred
                else:
                    
                    pred = prediccion_dif_media(i, j, k)
                    matriz_final[i][j] = pred

                    print "\nResultado prediccion - Usuario " + str(i) + " -> Item " + str(j) + " = " + str(pred) + "\n"

    return matriz_final


# -----------------------------------------------------------------------------
# EJECICION GENERAL DE PROGRAMA
# -----------------------------------------------------------------------------


# Gestion de los parametros de entrada
parser = argparse.ArgumentParser(description='Analisis de un sistema recomendador')
parser.add_argument('file', type=argparse.FileType('r'))
parser.add_argument('metrica',
                    choices=['pearson', 'euclidea', 'coseno']) #Luego analizo si tiene sentido o no

parser.add_argument('neighbors', type=int,
                    help="Indica el numero de vecinos a considerar en el analisis")

parser.add_argument('prediccion', 
                    choices=['simple', 'media'])

args = parser.parse_args()

#Lectura del fichero
linea_fichero = args.file.readlines() # Devuelve un vector de strings
matriz = [] # Matriz leida del fichero
usuarios_predecir = [] #Array con los usuarios de los que debemos predecir valores
for i in linea_fichero:
    linea = i.split()
    lineaux = []
    necesita_predecir = False
    for j in linea:
        if j != '-':
            aux = int(j)
        else:
            aux = j
            necesita_predecir = True
        lineaux.append(aux)
    if(necesita_predecir == True):
        usuarios_predecir.append(len(matriz))    
    matriz.append(lineaux)

#Creamos la matriz de similitudes vacia
matriz_similitudes = [ [ None for y in range(len(matriz)) ] for x in range( len(matriz)) ] #Matriz de similitud rellena de ceros

x = main(args.metrica , args.prediccion, args.neighbors)
print "--- MATRIZ CON LAS PREDICCIONES ---"
show_matriz(x)


