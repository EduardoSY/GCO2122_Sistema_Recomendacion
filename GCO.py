import argparse
import math
#Con type(variable) puedo ver el tipo de la variable.
#reduce hace magia

parser = argparse.ArgumentParser(description='Analisis de un sistema recomendador')
parser.add_argument('file', type=argparse.FileType('r'))
#parser.add_argument('metrica') #Luego analizo si tiene sentido o no

parser.add_argument('neighbors', type=int,
                    help="Indica el numero de vecinos a considerar en el analisis")

#parser.add_argument('produccion')

args = parser.parse_args()

#Lectura del fichero
matriz_fichero = args.file.readlines() # Devuelve un vector de strings
matriz = []

for i in matriz_fichero:
    linea = i.split()
    lineaux = []
    for j in linea:
        if j != '-':
            aux = int(j)
        else:
            aux = j
        lineaux.append(aux)
    matriz.append(lineaux)
print(matriz)

def valores_comunes(usuario_u, usuario_v):
    vector_usuario_u = []
    vector_usuario_v = []
    for i in range(len(matriz[usuario_u])):
      if(matriz[usuario_u][i] != '-' and matriz[usuario_v][i] != '-'):
          vector_usuario_u.append(matriz[usuario_u][i])
          vector_usuario_v.append(matriz[usuario_v][i])
    return vector_usuario_u, vector_usuario_v

def media(dataset):
    return sum(dataset) / float(len(dataset))

def coef_corr_pearson(usuario_u, usuario_v):
    vector_usuario_u, vector_usuario_v = valores_comunes(usuario_u, usuario_v)
    media_user_u = media(vector_usuario_u)
    media_user_v = media(vector_usuario_v)
    print "Usuario u media " + str(media_user_u)
    print "Usuario v media " + str(media_user_v)
    numerador = 0
    raiz_izq = 0
    sum_raiz_izq = 0
    raiz_der = 0
    sum_raiz_der = 0
    for i in range(len(matriz[usuario_u])):
        if ((matriz[usuario_u][i] != '-') and (matriz[usuario_v][i != '-'])): 
            numerador += ((matriz[usuario_u][i] - media_user_u) * (matriz[usuario_v][i] - media_user_v))
            sum_raiz_izq += (matriz[usuario_u][i] - media_user_u) ** 2
            sum_raiz_der += (matriz[usuario_v][i] - media_user_v) ** 2
    
    resultado = (numerador / (math.sqrt(sum_raiz_izq) * math.sqrt(sum_raiz_der)))
    return resultado


def dist_cos(usuario_u, usuario_v):
    numerador = 0
    suma_raiz_izq = 0
    suma_raiz_der = 0
    
    for i in range(len(matriz[usuario_u])):
        if ((matriz[usuario_u][i] != '-') and (matriz[usuario_v][i != '-'])): 
            numerador += matriz[usuario_u][i] * matriz[usuario_v][i]
            sum_raiz_izq += (matriz[usuario_u][i]) ** 2
            sum_raiz_der += (matriz[usuario_v][i]) ** 2

    resultado = (numerador / (math.sqrt(sum_raiz_izq) * math.sqrt(sum_raiz_der)))
    return resultado



vect1 = [1, 1, 2, 1, 1, 1, 1, 0, 0, 0]
vect2 = [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]


def dist_euclidea(usuario_u, usuario_v):
    resultado = 0
    for i in range(len(matriz[usuario_u])):
        if ((matriz[usuario_u][i] != '-') and (matriz[usuario_v][i != '-'])):  
            resultado += ((matriz[usuario_u][i] - matriz[usuario_v][i])**2)
    resultado = math.sqrt(resultado)
    return resultado


x = coef_corr_pearson(0,1)
print x
    