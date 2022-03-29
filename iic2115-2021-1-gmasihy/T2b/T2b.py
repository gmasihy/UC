#!/usr/bin/env python
# coding: utf-8

# Lamento no haber alcanzado a terminar la pregunta 1. Asistí a clases y estuve hasta el último minuto tratando, pero no me funcionó :(

# In[2]:


from collections import defaultdict, deque

class Nodo:
    def __init__(self, valor, padre=None):
        self.valor = valor
        self.padre = padre
        self.hijo_izquierdo = None
        self.hijo_derecho = None

    def __repr__(self):
        return 'padre: {0}, valor: {1}'.format(self.padre, self.valor)


class ArbolBinario:
    def __init__(self, nodo_raiz=None):
        self.nodo_raiz = nodo_raiz

    def agregar_nodo(self, valor):
        if self.nodo_raiz == None:
            self.nodo_raiz = Nodo(valor)
        else:
            temp = self.nodo_raiz
            agregado = False

            while not agregado:

                if valor <= temp.valor:
                    if temp.hijo_izquierdo == None:

                        temp.hijo_izquierdo = Nodo(valor, temp.valor)
                        agregado = True
                    else:

                        temp = temp.hijo_izquierdo
                else:
                    if temp.hijo_derecho == None:

                        temp.hijo_derecho = Nodo(valor, temp.valor)
                        agregado = True
                    else:

                        temp = temp.hijo_derecho

arbol = [(0,1,2),(4,None,6),(1,3,None),(2,4,5),]                        
T = ArbolBinario()
for i in arbol:
        T.agregar_nodo(i)

#def profundidad_arbol_binario(arbol):
#        profundidad = profundidad_arbol_binario(arbol)
#        return profundidad
#print(profundidad_arbol_binario(arbol))


# In[ ]:




