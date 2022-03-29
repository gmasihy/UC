#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import time #lo usé para probar tiempos de ejecución


# Los tres primeros problemas los resolví usando backtracking, mientras que para el último usé...
# Además, comenté algunas líneas en cada pregunta para facilitar la comprensión del código.

# # I. Los Cristaloides y su red del metro

# In[2]:


#t1 = time.time()  

def asignar(red,end):
    #en end se necesita diccionario con la primera línea y primer color
    supera_criterio = True
    #por estación que tenga la última línea con color
    for estacion in red[len(end)-1]:
        #se recorren líneas anteriores
        for linea in red[:len(end)-1]:
            #si está en esta linea y si los colores de la línea y el último son iguales
            if estacion in linea and end[str(linea)]==end[str(list(end)[-1])]:
                end[str(list(end)[-1])] += 1  #se agrega un color, porque la última línea coloreada...
                return asignar(red,end) #combina con el mismo color
    if len(red)==len(end):
        return list(end.values()) #retorno final
    else:
        sgte_linea = len(end) #última posición +1
        key = red[sgte_linea]
        end[str(key)] = 0
        return asignar(red,end)
    
def buscar_correspondencia(estacion,red): #busca el match estación/línea
    i = 0
    for linea in red:
        if estacion in linea:
            return i
        i += 1
        
def asignar_colores(lineas,combinaciones):
    red = lineas.copy()
    for interseccion in combinaciones: #se buscan las intersecciones. Para cada línea se recorre la red, para...
        n0 = buscar_correspondencia(interseccion[0],red) #ver si está
        n1 = buscar_correspondencia(interseccion[1],red)
        red[n0].append(interseccion[1])
        red[n1].append(interseccion[0])
    return asignar(red,{str(red[0]):0})

lineas = [[0, 1, 2], [3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
combinaciones = {(0, 10), (1, 6)}
colores = asignar_colores(lineas,combinaciones)

#t2 = time.time()
#print(t2-t1)


# In[3]:


if __name__ == "__main__":
    print(colores)


# # II. Sopa de letras

# In[4]:


#t1 = time.time()

def resolver_multiple(sopa, texto, punto, end='',END=''):
    #end son los puntos hasta ahora, i.e. va cambiando. Mientras que END representa todas las soluciones
    ultima_posicion = len(end) -1
    if END == '':
        END = []
    if end == '':
        end = [punto]
    else:
        ult_letra_texto = texto[ultima_posicion] #se verifica que la última letra del texto coincida con la...
        coor_i = punto[0] #última posición.
        if coor_i <0 or coor_i>=len(sopa[0]): #si la coordenada i se pasa de rango, retorno vacío
            return
        coor_j = punto[1]
        if coor_j <0 or coor_j>=len(sopa[0]): #lo mismo para j, debe estar en el tablero
            return
        if punto in end[:-1]:
            return
        ult_letra_sopa  = sopa[coor_i][coor_j]
        if ult_letra_texto != ult_letra_sopa: #se verifica si cumple o no 
            return #retorno None por defecto
    if len(end)==len(texto):
        END.append(end)
    else:
        resultado = [] #a continuación se forman los 8 movimientos posibles:
        punto_ = (punto[0]+1,punto[1]) #abajo
        resolver_multiple(sopa, texto, punto_, end.copy()+[punto_],END)
        punto_ = (punto[0]-1,punto[1]) #arriba
        resolver_multiple(sopa, texto, punto_, end.copy()+[punto_],END)
        punto_ = (punto[0],punto[1]+1) #derecha
        resolver_multiple(sopa, texto, punto_, end.copy()+[punto_],END)
        punto_ = (punto[0],punto[1]-1) #izquierda
        resolver_multiple(sopa, texto, punto_, end.copy()+[punto_],END)
        punto_ = (punto[0]-1,punto[1]-1) #izq sup
        resolver_multiple(sopa, texto, punto_, end.copy()+[punto_],END)
        punto_ = (punto[0]-1,punto[1]+1) #der sup
        resolver_multiple(sopa, texto, punto_, end.copy()+[punto_],END)
        punto_ = (punto[0]+1,punto[1]-1) #izq inf
        resolver_multiple(sopa, texto, punto_, end.copy()+[punto_],END)
        punto_ = (punto[0]+1,punto[1]+1) #der inf
        resolver_multiple(sopa, texto, punto_, end.copy()+[punto_],END)
        return END
    
def encontrar_ocurrencias(sopa, texto): #proceso inicial, en el que considera todos los puntos de partidas...
    gran_sopa='\n'.join(sopa) #por lo que si encuentro más soluciones, tengo un resultado que parte en vacío...
    cantidad_puntos_iniciales = gran_sopa.count(texto[0]) #y a este se le agrega todo lo que encuentre
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    n_columnas_t = n_columnas + 1 #por el '\n'
    resultados = []
    ubicacion = 0
    for r in range(cantidad_puntos_iniciales):
        ubicacion = gran_sopa.index(texto[0],ubicacion)
        i = ubicacion//n_columnas_t
        j = ubicacion%n_columnas_t
        punto = (i,j)
        resultados += resolver_multiple(sopa, texto, punto)
        ubicacion += 1
    return resultados

sopa = ["LAMXB", "AOEYF", "FCHTB", "GFKAR", "POSFD"]
texto = "HOLA"
posiciones = encontrar_ocurrencias(sopa, texto)

#t2 = time.time()
#print(t2-t1)


# In[5]:


if __name__ == "__main__":
    print(*posiciones, sep="\n")


# # III. Qué evaluaciones conviene hacer

# In[6]:


#t1 = time.time()

def programar_evaluaciones(evaluaciones,end=[],suma=0):
    #end es una lista de tuplas que satisface el formato del output del enunciado
    #suma es el total de ponderaciones
    if len(end)==0: #caso inicial. Se revisa end, si es que es vacía no se hace nada.
        pass
    elif end[-1][1]<len(end): #si lo que queda de plazo es menor que el largo de la lista, entonces ya no queda plazo...
        eva_pond_menor = end[0] #para resolver esa tarea, porque ocupa 1 día. Aunque no significa que no se agregue al resultado, sino que... 
        for eva in end[1:]: #se busca entre todos los resultados al que pondere menos.
            if eva_pond_menor[2] > eva[2]:
                eva_pond_menor = eva
            elif eva_pond_menor[2] == eva[2] and eva_pond_menor[1] > eva[1]: #si dos procesos tienen la misma ponderación...
                eva_pond_menor = eva #se reemplaza el de menor ponderación al que tenga más plazo, i.e. se optimiza por menor plazo...
        end.remove(eva_pond_menor) #y por mayor ponderación.
    if len(evaluaciones)==0:
        pond = 0
        lista = []
        for eva in end: #eva es la tupla entera que se entrega --> nombres,dias,ponderación
            pond += eva[2]
            lista.append(eva[0])
        return lista,pond/suma #pero se retorna la lista de puros nombres y la nota ponderada.
    eva_menor = evaluaciones[0]
    for eva in evaluaciones[1:]:
        if eva[1] < eva_menor[1]: #si es que no termina, se toma la menor evaluación, i.e. la que está arriba... 
            eva_menor = eva #como simulando una cola. Se busca el menor plazo.
        elif eva[1] == eva_menor[1] and eva[2] > eva_menor[2]: #se compara con todo el resto
            eva_menor = eva
    x = evaluaciones.index(eva_menor) #busco el índice de la evaluación "x" y luego me lo salto para la recursión.
    return programar_evaluaciones(evaluaciones[:x]+evaluaciones[x+1:],end+[eva_menor],suma+eva_menor[2]) #al camino de resultados le agrego la tupla menor y a la suma de resultados le agrego el valor de esa tupla.

evaluaciones = [('Tarea4',9,15),('Control1',2,2),('I1',5,18),('Control3',7,1),
                ('Control2',4,25),('Taller1',2,20),('Tarea2',5,8),('Tarea3',7,10),
                ('Taller2',4,12),('Tarea1',3,5)]
orden, nota = programar_evaluaciones(evaluaciones)
nota = round(nota,2) #redondeo la nota a dos decimales

#t2 = time.time()
#print(t2-t1)


# In[7]:


if __name__ == "__main__":
    print(orden)
    print(nota)


# # IV. Cómo ordenar el proceso de vacunación

# In[8]:


#import sys
#!{sys.executable} -m pip install numpy #lo usé para poder importar numpy en jupyter


# In[9]:


#t1 = time.time()

from itertools import permutations as per
import numpy as np

def un_orden(rel,REL=None):
    if REL == None: 
        REL = rel.copy() #REL es una copia de las relaciones
    if len(rel)==1: #caso base: queda una relación
        return list(rel[0])
    else:
        m = len(rel)//2  #saco el punto medio y lo divido en un orden hacia atrás y adelante
        i = un_orden(rel[:m],REL) #está inspirado en dividir y conquistar
        d = un_orden(rel[m:],REL)
        L = i.copy() #hago una copia del izquierdo para no alterar lo que hay en las otras relaciones. Y a esta...
        for elemento in d: #copia le agrego todos los elementos que hay en la parte derecha sin que se repitan
            if elemento not in L:
                L.append(elemento)
        return revision_orden(L,REL)
    
def revision_orden(sec,REL): #reviso todas las relaciones en la secuencia.
    for r in REL: 
        antes = r[0]
        despues = r[1]
        if (antes in sec) and (despues in sec): #siempre que hayan dos en la secuencia, pero con el orden cambiado...
            x = sec.index(antes)
            y = sec.index(despues)
            if x>y:
                sec[x],sec[y] = sec[y],sec[x] #se cambia el orden en la secuencia y vuelvo a revisar.
                return revision_orden(sec,REL)
    return sec

def comprobar_error(relaciones): #acá ocupé una matriz de adyacencia, para encontrar ciclos. Porque al hacer multiplicaciones...
    nodos = []                   #hasta encontrar la matriz de ceros con unos en la diagonal, entonces tengo un ciclo.
    for rel in relaciones:
        nodos.extend(list(rel))
    nodos = list(set(nodos))
    nodos.sort()
    n = len(nodos)
    matriz_adj = np.zeros((n,n))
    
    for rel in relaciones:
        x = nodos.index(rel[0])
        y = nodos.index(rel[1])
        matriz_adj[x][y] = 1

    #compruebo según matriz de adyacencia
    #si al calcular A*A*A*A.... hasta encontrar
    #matriz de ceros, se encuentran 1s en la diagonal,
    #entonces existe un ciclo, compuesto por los nodos representados
    matrices = [matriz_adj]
    while not np.equal(matrices[-1], np.zeros((n,n))).all(): #compara dos matrices con la función equal...
        matriz_temp = matrices[-1].dot(matriz_adj) #y con .all evalúa si todas la posiciones tienen valor True...
        diagonal = list(np.diagonal(matriz_temp)) #Entonces mientras haya una con False, i.e. no encuentra la matriz de ceros,...
        pos = 0                                  #continuará la búsqueda.
        culpables = []
        for x in range(diagonal.count(1)): #recorro todos los unos que estén en la diagonal y los agrego a culpables...
            pos = diagonal.index(1,pos)  #si es que es True es porque hay culpables. 
            culpables.append(nodos[pos]) #lo nombré "culpables", porque son los responsables de que se genere un ciclo.
            pos += 1
        if len(culpables)>0:
            return [True,culpables]
        else:
            matrices.append(matriz_temp) #si es no hay culpables, agrego a las matrices que he recorrido la matriz temporal.
    return [False,None] #se van agregando matrices para luego ir multiplicandolas.

def ordenes_vacunacion(relaciones):
    error = comprobar_error(relaciones) #se comprueba que haya error.
    if error[0]:
        return error[1]
    #se ha pasado la comprobación
    ordenes = []
    per_rel = list(per(relaciones)) #Aviso: esto es un poco ineficiente para instancias grandes, pero fue lo único que encontré que se adaptaba a la estructura de mi código.
    #se permutan relaciones
    #y se forman caminos por función del tipo
    #dividir y conquistar
    for rell in per_rel: #recorro las relaciones en todos los órdenes posibles
        lista = un_orden(list(rell)) #luego la lista va a ser un orden de esas relaciones. Si esa lista no está...
        if lista not in ordenes: #en los órdenes que ya tengo guardados, la guardo. Pero antes compruebo que no se repita.
            ordenes.append(lista)
    return ordenes

relaciones = [(0,6),(1,2),(1,4),(1,6),(3,0),(3,4),(5,1),(7,0),(7,1)]
resultado = ordenes_vacunacion(relaciones)

if __name__ == "__main__":
    print(*resultado,sep='\n')
    print()

relaciones = [(0,6),(1,2),(1,4),(1,6),(3,0),(3,4),(5,1),(6,3),(7,0),(7,1)]
resultado = ordenes_vacunacion(relaciones)

if __name__ == "__main__":
    print(resultado)

#t2 = time.time()
#print(t2-t1)

