import sqlite3

with sqlite3.connect("./sqlite/prueba.db") as con:
    cursor = con.cursor()
    usuarios = {
        (2, "Jonatan"),
        (3, "Elif"),
    }
    cursor.executemany(
        "insert into usuarios values(?,?)",
        usuarios,
    )