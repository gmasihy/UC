#!/usr/bin/env python
# coding: utf-8

# In[4]:


#P1
#Se define una función que genera la lista de tuplas pedida.
#Esta crea un diccionario a partir de una lista de palabras entregada y cuantifica la 
#cantidad de ocurrencias de las llaves, para luego crear una lista de tuplas:


def retorno_de_tuplas(a):
    diccionario = {}

    for palabra in a:

        if palabra not in diccionario:

            diccionario[palabra] = 1

        else:
            diccionario[str(palabra)] += 1

    vacia = []

    for i in diccionario:
        tuplita = (i,diccionario[i])
        vacia.append(tuplita)
    #print(vacia)

    return vacia

palabras = ["perro","gato","perro","perro","gato","pato"] # <- lista de prueba que usé

retorno_de_tuplas(palabras)


# In[5]:


#P2

#Lamentablemente no alcancé a terminar esta parte, no me resulta. Pero esto es lo que se me ocurrió:

numeros = [2,3,4,6,7,12,13,15,5,17,14,22]

trios = []
for i in numeros:
    for j in numeros:
        k = i**2+j**2
        if k in numeros:
            tupli = (i,j,k)
            trios.append(tupli)
print(trios) #no imprime los valores que quiero


# In[ ]:




