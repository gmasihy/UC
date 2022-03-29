#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import sqlite3
import csv


# M0: Para esta parte, me guié del código entregado en la pauta del taller 3b.

# In[2]:


with open('movies.json',encoding = 'utf8') as movies_file:
    movies = json.load(movies_file)


# In[3]:


connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE Movies(mid INTEGER PRIMARY KEY, mtitle TEXT, myear INTEGER)")
cursor.execute("CREATE TABLE Actors(aid INTEGER PRIMARY KEY, aname TEXT)")
cursor.execute("CREATE TABLE Genres(gid INTEGER PRIMARY KEY, genre TEXT)")
cursor.execute("CREATE TABLE ActorsMovies(actor_id INTEGER, movie_id INTEGER, FOREIGN KEY (actor_id) REFERENCES Actors, FOREIGN KEY (movie_id) REFERENCES Movies)")
cursor.execute("CREATE TABLE GenresMovies(genre_id INTEGER, movie_id INTEGER, FOREIGN KEY (genre_id) REFERENCES Genres, FOREIGN KEY (movie_id) REFERENCES Movies)")

connection.commit()
connection.close()


# In[4]:


connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

mid = 1
aid = 1
gid = 1
genres = {}
actors = {}

for movie in movies:

    mtitle = movie["title"]
    myear = movie["year"]

    cursor.execute("INSERT INTO Movies VALUES (?,?,?)", (mid, mtitle, myear))

    for genre in movie["genres"]:
        if genre not in genres:
            genres[genre] = gid
            cursor.execute("INSERT INTO Genres VALUES (?,?)", (gid, genre))
            gid += 1
        cursor.execute("INSERT INTO GenresMovies VALUES (?,?)", (genres[genre], mid))

    for actor in movie["cast"]:
        if actor != "." and actor != "]" and actor != "Academy Award for Best Supporting Actress" and actor != "(" and actor != ")" and actor != "$119" and actor != "and" and actor != "500" and actor != "000" and actor != "[1]" and actor != "[2]" and actor != "$116" and actor!= "[3]" and actor != "[4]" and actor != "[5]" and actor != "[6]" and actor != "[7]" and actor != "[8]" and actor != "[9]" and actor != "[10]" and actor != "$89" and actor != "$86" and actor != "273" and actor != "333" and actor != "$79" and actor != "666" and actor != "653" and actor != "$47" and actor != "542" and actor != "841" and actor != "285" and actor != "152" and actor != "$45" and actor != "$43" and actor != "411" and actor != "063" and actor != "008" and actor != "075" and actor != "$39" and actor != "552" and actor != "the life of Jonathan Caouette" and actor != "the life and death of" and actor != "11" and actor != "and its relations with the" and actor != "in" and actor != "a" and actor != "by" and actor != "-":
            if actor not in actors:
                actors[actor] = aid
                cursor.execute("INSERT INTO Actors VALUES (?,?)", (aid, actor))
                aid += 1
            cursor.execute("INSERT INTO ActorsMovies VALUES (?,?)", (actors[actor], mid))

    mid += 1

connection.commit()
connection.close()


# M1

# In[5]:


import sys #tuve que usar esto para poder importar pyrematch, ya que con !pip3 no me funcionó
get_ipython().system('{sys.executable} -m pip install pyrematch')
get_ipython().system('{sys.executable} -m pip install pyrematch')


# In[6]:


import urllib.request as req
import ssl
import pyrematch as re
import bs4
import sqlite3


# In[7]:


connection = sqlite3.connect('movies.db')
cursor = connection.cursor()
cursor.execute('select * from Actors')
lista_actores = []
for reg in cursor:
    lista_actores.append(reg[1])
cursor.execute('select * from Movies')
lista_peliculas = []
for reg in cursor:
    lista_peliculas.append(reg[1])
connection.commit()
connection.close()


# In[8]:


lista_actores


# In[9]:


lista_peliculas


# In[10]:


def buscar_fecha(trs):
    patron = '(>)!r{Born}(<)'
    patron_f = "(^|\D)!f{\d+{1,4}\-\d+{1,2}\-\d+{1,4}}($|\D)" 
    regex   = re.compile(patron)
    regex_f = re.compile(patron_f)
    for tr in trs:
        m = regex.find(str(tr))
        if m:
            td = tr.find('td')
            m_f = regex_f.find(td.text)
            if m_f:
                return m_f.group('f')
            else:
                return td.text.strip()
    return ''


# In[11]:


def buscar_director(trs):
    patron = '(>)!r{Directed by}(<)'
    regex   = re.compile(patron)
    for tr in trs:
        m = regex.find(str(tr))
        if m:
            td = tr.find('td')
            return td.text.strip()
    return ''


# In[12]:


#se hizo prueba con 50 ultimos ya que hay mas coincidencias
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}


# In[13]:


def obtener_texto(link):
    respuesta = req.Request(link,headers=headers)
    return req.urlopen(respuesta,context=ssl.SSLContext()).read().decode('utf-8')
#obtener_texto('https://en.wikipedia.org/wiki/{}'.format(lista_peliculas[-50].replace(' ','_')))


# Usé el query de Wikipedia y no su librería directamente, ya que descubrí que así se demoraba la mitad. Lo tuve que hacer, porque mi computador es demasiado lento y me estresaba que se congelara cada vez que probaba una consulta

# In[14]:


directores_peli = []
for pelicula in lista_peliculas[-50:]:
    try:
        link = 'https://en.wikipedia.org/wiki/{}'.format(pelicula.replace(' ','_'))
        texto = obtener_texto(link)
        #en las ramas tr hay relaciones de tabla 
        #ej: nace -> 21-05-1815
        #   tr{th -> td}
        #tr alverga a th y td
        sopa = bs4.BeautifulSoup(texto)
        #todos los tr #tabla linea por linea
        trs = sopa.findAll('tr')
        directores_peli.append(buscar_director(trs).replace("'",""))
    except:
        directores_peli.append('')


# In[15]:


directores_peli


# In[16]:


nacimiento = []
for actor in lista_actores[-50:]:
    actor = actor.replace(' ','_')
    link = f'https://en.wikipedia.org/wiki/{actor}'
    try:
        texto = obtener_texto(link)
        sopa = bs4.BeautifulSoup(texto)
        trs = sopa.findAll('tr')
        nacimiento.append(buscar_fecha(trs).replace("'",""))
    except:
        nacimiento.append('')


# In[17]:


nacimiento


# In[18]:


connection = sqlite3.connect('movies.db')
cursor = connection.cursor()
cursor.execute('ALTER TABLE Actors ADD COLUMN fecha_naciemiento TEXT;')
cursor.execute('SELECT aid FROM Actors')
registros = list(cursor).copy()
for i in range(50):
    aid = registros[-50:][i][0]
    cursor.execute(f"update Actors set fecha_naciemiento='{nacimiento[i]}' WHERE aid={aid};")
cursor.execute('ALTER TABLE Movies ADD COLUMN director TEXT;')
cursor.execute('SELECT mid FROM Movies')
registros = list(cursor).copy()
for i in range(50):
    mid = registros[-50:][i][0]
    cursor.execute(f"update Movies set director='{directores_peli[i]}' WHERE mid={mid};")
connection.commit()
connection.close()


# M2

# In[19]:


def consultar(consulta):
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()
    cursor.execute(consulta)
    for reg in list(cursor):
        print(reg)
    connection.commit()
    connection.close()


# Consulta 1

# In[20]:


consulta='select myear, count(*) as cuenta from Movies group by myear order by cuenta DESC LIMIT 3'
consultar(consulta)


# Consulta 2

# In[21]:


consulta ='select Actors.aname,(max(Movies.myear)-min(Movies.myear)) as trayectoria ' 
consulta+='from Actors, Movies, ActorsMovies where Actors.aid=ActorsMovies.actor_id '
consulta+='and ActorsMovies.movie_id=Movies.mid group by ActorsMovies.actor_id order by trayectoria DESC '
consulta+='LIMIT 5'
consultar(consulta)


# Consulta 3: esta consulta no la alcancé a hacer y preferí no ponerla incompleta. La cantidad de interacciones entre múltiples tablas para responderla nunca me cargaba en el computador. Lo siento :(

# In[22]:


consulta ="select aname from Actors" #lo usé para chequear que no hubieran errores de formato en los nombres
consultar(consulta)

