import sqlite3

con = sqlite3.connect("./sqlite/prueba.db")
cursor = con.cursor()
cursor.execute(
    """
        CREATE TABLE IF not exists usuarios
        (id INTERGER primary key, nombre VARCHAR(50));
    """
)
con.commit()
con.close()