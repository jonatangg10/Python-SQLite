# SQL lite es una base de datos ligera e independiente
# Los datos se guardan en un directorio

import sqlite3

with sqlite3.connect("./sqlite/prueba.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuarios")
    print(cursor.fetchall())