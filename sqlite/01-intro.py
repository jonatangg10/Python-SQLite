# SQL lite es una base de datos ligera e independiente
# Los datos se guardan en un directorio prueba.db
# Ejecuta del 01 al 07 siguiendolos en orden

import sqlite3

con = sqlite3.connect("./sqlite/prueba.db")
con.close()