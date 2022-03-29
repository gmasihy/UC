#!/usr/bin/env python
# coding: utf-8

# In[46]:


import sqlite3
import csv


# In[47]:


connection = sqlite3.connect('data.db')
cursor = connection.cursor()


# Consulta 1

# In[48]:


cursor.execute("SELECT E.nivel, AVG(E.edad)                 FROM Estudiantes E                WHERE E.nivel != 'JR'                 GROUP BY E.nivel")

print(cursor.fetchall())
connection.close()


# Consulta 2

# In[49]:


connection = sqlite3.connect('data.db') 
cursor = connection.cursor()

cursor.execute('SELECT DISTINCT E.nombre                FROM Estudiantes E, Cursos C, Inscritos I                 WHERE NOT (E.num = I.num_est AND C.nombre = I.nombre_curso)')

for r in cursor:
    print(r[0])
connection.close()


# Consulta 3

# In[50]:


connection = sqlite3.connect('data.db') 
cursor = connection.cursor()

cursor.execute('SELECT DISTINCT P.nombre                FROM Profesores P, Cursos C, Inscritos I, Estudiantes E                 WHERE (E.num = I.num_est AND C.nombre = I.nombre_curso AND I.num_est < 5)                GROUP BY P.nombre                 HAVING I.num_est >= 1')

for r in cursor:
    print(r[0])
connection.close()


# Consulta 4

# In[51]:


connection = sqlite3.connect('data.db') 
cursor = connection.cursor()

cursor.execute('SELECT DISTINCT C.nombre                FROM Inscritos I, Cursos C                 WHERE (I.num_est >= 5 or C.sala = "R128")')

for r in cursor:
    print(r[0])
    
connection.close()


# In[ ]:




