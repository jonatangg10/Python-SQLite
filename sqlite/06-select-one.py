import sqlite3

with sqlite3.connect("./sqlite/prueba.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuarios")
    print(cursor.fetchone())