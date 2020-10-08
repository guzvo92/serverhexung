

import sqlite3

conexion = sqlite3.connect('../db.sqlite3')
cursor = conexion.cursor()


cursor.execute('DROP TABLE guildchars_dbchar10')

cursor.execute("SELECT * FROM blog_post")
x = cursor.fetchall()
for item in x:
    print(item)

conexion.commit()
