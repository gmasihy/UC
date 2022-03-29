#!/usr/bin/env python
# coding: utf-8

# En primer lugar, cargué el archivo "movies.json":

# In[18]:


import json
with open('movies.json',encoding='utf8') as movies_file:
    movies = json.load(movies_file)


# Misión 1: "Modelación de entidades". 
# Se definen las clases "Pelicula", "Actor" y "Genero":

# In[30]:


class Pelicula:

    def __init__(self,titulo,ano,reparto,genero):
        self.titulo = titulo
        self.ano = ano
        self.reparto = reparto
        self.genero = genero
    


class Actor:

    def __init__(self,elenco,ano_aparicion):
        self.elenco = elenco
        self.ano_aparicion = ano_aparicion
        self.lista_actuaciones = []
        self.par_actor_ano = ()
    
    def add_tupla(self):
        self.lista_actuaciones.append(self.par_actor_ano)
        

class Genero:

    def __init__(self,lista_generos):
        self.lista_generos = []

    def lista_de_generos(self):
        for gen in Pelicula.genero:
            self.lista_generos.append(gen)


# Misión 2: "Carga de datos". Se extraen los datos y se cargan en los objetos correspondientes:

# In[46]:


peliculas = []
for movie in movies:
    a = Pelicula(movie["title"],movie["year"],movie["cast"],movie["genres"])
    peliculas.append(a)

actores = []
for movie in movies:
    b = Actor(movie["cast"],movie["year"])
    actores.append(b)

generos = []
for movie in movies:
    c = Genero(movie["genres"])
    generos.append(c)


# Misión 3: "Consultas sobre los datos". Se intenta responder las consultas pedidas:

# Consulta 1:

# In[54]:


### metodo para encontrar los 5 generos mas populares

generos = []
contador_rep = 0
for j in movies:
    generos += j['genres']

#print(generos)

aux = []
bla = {}
for i in generos:
    if i not in aux:
        a = generos.count(i)
        bla[i] = a
#print(bla)
## bla es el diccionario que contiene los generos como llaves y la cantidad de peliculas que pertenecen a ese genero como valores

bla2 = {}
j = 1
b = sorted(bla.values())
mayor = max(bla.values())

for rep in bla:
    if bla[rep] == mayor and j <= 5:
        bla2[rep] = mayor
        j += 1
    elif bla[rep] == mayor-1 and j <= 5:
        bla2[rep] = mayor-1
        j += 1
    elif bla[rep] == mayor-2 and j <=5:
        bla2[rep] = mayor-2
        j += 1

#print(bla2)
### bla2 es un diccionario que contiene los 5 generos mas populares como llaves y su cantidad de repeticiones como valores


# Consulta 2:

# In[56]:


#posible metodo para obtener los tres anos que mas peliculas se hacen

anos = []
contador_rep = 0
for j in movies:
    anos.append(j['year'])

aux = []
bla = {}
for i in anos:
    if i not in aux:
        a = anos.count(i)
        bla[i] = a

#print(bla)
#bla es el diccionario que contiene los anos como llaves y la cantidad de peliculas realizadas por ano como valores

mayor = max(bla.values())

bla2 = {}
i = 1
b = sorted(bla.values())

for rep in bla:
    if bla[rep] == b[len(b)-1] and i <= 3:
        bla2[rep] = b[len(b)-1]
        i += 1
for rep in bla:
    if bla[rep] == b[len(b)-2] and i <= 3:
        bla2[rep] = b[len(b)-2]
        i += 1
for rep in bla:
    if bla[rep] == b[len(b)-3] and i <= 3:
        bla2[rep] = b[len(b)-3]
        i += 1

#print(bla2)
#bla2 = diccionario que contiene los tres años con mas ocurrencias


# El resto de las consultas preferí no incluirlas en el código, pues tenían algunos errores importantes.

# In[ ]:





# In[ ]:




