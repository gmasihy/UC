#!/usr/bin/env python
# coding: utf-8

# Pregunta 1

# Al seguir rigurosamente los pasos dados en el enunciado, se llegó a la siguiente función:

# In[4]:


def calcular_max_long(a):
    maximo = 0
    stack = [-1]
    for i in range(len(a)):

        if a[i] == "(":
            stack.append(i)

        if a[i] == ")":
            stack.pop()
            if len(stack) == 0:
                stack.append(i)

        largo = i - stack[-1]
        if largo > maximo:
            maximo = largo

    return maximo

parentesis = "(((())"

max_long = calcular_max_long(parentesis)

print(max_long)


# Pregunta 2
# 

# Esta parte no la alcancé a terminar. Esto es lo que pude hacer:

# In[7]:


from collections import deque

grafo = [(0,6),(0,1),(1,6),(1,5),(1,2),(2,3),(3,4),(5,2),(5,3),(5,4),(6,5),(7,6),(7,1)]

origen = 0
destino = 3
m = 4

Q = deque()
for i in grafo:
    Q.append(i)

def caminos_largo_m(grafo,origen,destino,m):
    Q = deque()
    for i in grafo:
        Q.append(i)


# In[ ]:




