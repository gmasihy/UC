import sqlite3
import json
with open('movies.json',encoding = 'utf8') as movies_file:
    movies = json.load(movies_file)

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Peliculas(name TEXT, year INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS Reparto(name TEXT, cast LIST)")
cursor.execute("CREATE TABLE IF NOT EXISTS Generos(name TEXT, genres LIST)")

for elemento in movies:
    cursor.execute("INSERT INTO Peliculas VALUES (elemento[0],elemento[1])")
    cursor.execute("INSERT INTO Reparto VALUES (elemento[0],elemento[2])")
    cursor.execute("INSERT INTO Generos VALUES (elemento[0],elemento[3])")

cursor.execute("CREATE TABLE IF NOT EXISTS Actuacion (id_actor: INTEGER, id_pelicula: INTEGER, actua: BOOL)")

connection.commit()
connection.close()

