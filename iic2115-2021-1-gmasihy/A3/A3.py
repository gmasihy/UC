#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import csv


# In[2]:


connection = sqlite3.connect('A3.db') 
cursor = connection.cursor()


# Misión 1

# In[3]:


cursor.execute("CREATE TABLE Empleados(eid INTEGER, enombre STRING, edad INTEGER,                 sueldo FLOAT)")
with open('empleado.txt') as e:
    for line in csv.reader(e):
        cursor.execute('INSERT INTO empleados VALUES (:eid,:enombre,:edad,:sueldo)', 
                           {"eid": line[0], "enombre": line[1], "edad": line[2], "sueldo": line[3]})


# In[4]:


cursor.execute("CREATE TABLE Trabaja_en(id_empleado INTEGER, id_dpto INTEGER, porcentaje_tiempo INTEGER)")
with open('trabaja_en.txt') as t:
    for line in csv.reader(t):
            cursor.execute('INSERT INTO trabaja_en VALUES (:id_empleado,:id_dpto,:porcentaje_tiempo)', 
                           {"id_empleado": line[0], "id_dpto": line[1], "porcentaje_tiempo": line[2]})


# In[5]:


cursor.execute("CREATE TABLE Departamentos(did INTEGER, dnombre STRING, presupuesto FLOAT, id_jefe INTEGER)")
with open('departamento.txt') as d:
    for line in csv.reader(d):
            cursor.execute('INSERT INTO departamentos VALUES (:did,:dnombre,:presupuesto,:id_jefe)', 
                           {"did": line[0], "dnombre": line[1], "presupuesto": line[2], "id_jefe": line[3]})


# In[6]:


connection.commit()


# Misión 2

# Consulta 1: Encuentre el nombre y la edad de cada empleado que trabaja en los departamentos de Software y Hardware.

# In[7]:


connection = sqlite3.connect('A3.db') 
cursor = connection.cursor()
cursor.execute("SELECT DISTINCT E.enombre, E.edad                 FROM Empleados E, Departamentos D, Trabaja_en T                 WHERE E.eid = T.id_empleado AND D.did = T.id_dpto AND D.dnombre = 'Software' AND                 (SELECT D.dnombre                 FROM Empleados E, Departamentos D, Trabaja_en T                 WHERE D.dnombre = 'Hardware' AND E.eid = T.id_empleado AND D.did = T.id_dpto) = 'Hardware'")
for r in cursor:
    print(r[0],r[1])
connection.close()


# Consulta 2: Encuentre el nombre de los jefes que administran los departamentos con el presupuesto máximo.

# In[8]:


connection = sqlite3.connect('A3.db') 
cursor = connection.cursor()
cursor.execute("SELECT DISTINCT E.enombre                 FROM Empleados E, Departamentos D, Trabaja_en T                 WHERE E.eid = D.id_jefe AND                 (SELECT MAX(D.presupuesto)                 FROM Empleados E, Departamentos D, Trabaja_en T                 WHERE E.eid = D.id_jefe) = D.presupuesto ")
for r in cursor:
    print(r[0])
connection.close()


# Consulta 3: Encuentre el nombre de los empleados cuyo sueldo excede el presupuesto de todos los departamentos en los que trabaja.

# In[9]:


connection = sqlite3.connect('A3.db') 
cursor = connection.cursor()
cursor.execute("SELECT E.enombre                 FROM Empleados E, Departamentos D, Trabaja_en T                 WHERE E.eid = T.id_empleado AND D.did = T.id_dpto AND E.sueldo > D.presupuesto ")
for r in cursor:
    print(r[0])
connection.close()


# Consulta 4: Para cada departamento con dedicación del personal EQUIVALENTE a al menos 20 empleados a tiempo completo, encuentre el nombre del departamento y la cantidad de empleados.

# In[10]:


connection = sqlite3.connect('A3.db') 
cursor = connection.cursor()
cursor.execute("SELECT D.dnombre, COUNT(E.eid)                 FROM Empleados E, Departamentos D, Trabaja_en T                 WHERE E.eid = T.id_empleado AND D.did = T.id_dpto                 GROUP BY D.did                 HAVING SUM(T.porcentaje_tiempo) >= 2000 ")
for r in cursor:
    print(r)
connection.close()


# In[ ]:




