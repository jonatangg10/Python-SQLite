import sqlite3

with sqlite3.connect("./sqlite/prueba.db") as con:
    cursor = con.cursor()
    cursor.execute(
        "insert into usuarios values(?,?)",
        (1, "Hola mundo")
    )