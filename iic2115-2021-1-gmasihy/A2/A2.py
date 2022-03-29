#!/usr/bin/env python
# coding: utf-8

# P1

# Para esta pregunta transformé el string original a un stack y creé una lista vacía. Con un for agregué el último elemento del stack a la lista vacía y luego eliminé ese elemento del stack. Finalmente, transformé la lista resultante al string inverso.

# In[15]:


def invertir_string(string_original):
    vacia = []
    stack = []
    stack[:0] = string_original
    for i in range(len(stack)):
        vacia.append(stack[-1])
        stack.pop()
    return ''.join(vacia)

string_original = "programación_como_herramienta_para_la_ingeniería"
string_inverso = invertir_string(string_original)


# In[16]:


if __name__ == "__main__":
    print(string_inverso)


# P2
# 

# Para esta pregunta me guié en la materia de algoritmos de ordenamiento del capítulo 2 b).lo que hice fue crear un algoritmo sensillo que toma la lista que ingresa a la función y la deja ordenada de manera ascendente con todos sus valores positivos. La función retorna el producto entre los dos últimos valores de la nueva lista. 

# In[22]:


def maximo_producto_absoluto(lista):
    nueva_lista = []
    for i in lista:
        nueva_lista.append(abs(i))
    nueva_lista.sort()
    return nueva_lista[len(nueva_lista)-1] * nueva_lista[len(nueva_lista)-2]

lista = [-10, -3, 4, 6, -2]
max_prod = maximo_producto_absoluto(lista)


# In[23]:


if __name__ == "__main__":
    print(max_prod)


# P3
# 

# Para esta pregunta me guié de los conceptos "dividir y conquistar" y usé recursión. Tomé como valor más cercano a la mitad del número dado y luego iteré en un while sacando la mitad del número resultante y corrobarando la condición de salida. Es importante señalar que la condición del "if not" debe ser >1, ya que el número que buscamos se trata de uno natural. Esto reduce significativamente la cantidad de iteraciones O(log(n)), ya que de haber puesto una condición más exacta, e.g. "if curr*curr == numero:" este algoritmo se hubiese quedado en el loop.

# In[32]:


def calcular_raiz(numero):
    mas_cercano = numero/2
    while True:
        curr =  (mas_cercano + (numero / mas_cercano))/2
        if not curr*curr - numero > 1:
            return int(curr)
        mas_cercano = curr

numero = 17
raiz = calcular_raiz(numero)


# In[33]:


if __name__ == "__main__":
    print (raiz)
    


# P4

# Para que un nodo fuera accesible descde cualquier nodo, bastaba comprobar que hubiera un 1 en todas las fias y columnas

# In[38]:


def caminos_desde_todos(grafo):
    condiciones_cumplidas = 0
    for fila in grafo:
        if 1 in fila:
            condiciones_cumplidas += 1
        else:
            return False
        for i in range(len(fila)):
            if fila[i] == 1:
                condiciones_cumplidas +=1

    if condiciones_cumplidas >= 2:
        return True
    else:
        return False

    
grafo = [[0,0,0,0,1],[1,0,1,0,0],[0,1,0,0,1],[0,1,1,0,0],[0,0,0,1,0]]
se_puede = caminos_desde_todos(grafo)


# In[39]:


print(se_puede)


# In[ ]:





# In[ ]:




