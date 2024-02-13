import sqlite3

with sqlite3.connect("./sqlite/prueba.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
            CREATE TABLE IF not exists usuarios
            (id INTERGER primary key, nombre VARCHAR(50));
        """
    )