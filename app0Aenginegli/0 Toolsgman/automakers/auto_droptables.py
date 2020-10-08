
import sqlite3
conexion = sqlite3.connect('../db.sqlite3')
cursor = conexion.cursor()

cursor.execute('DROP TABLE guildchars_dbchar0')
cursor.execute('DROP TABLE guildchars_dbchar1')
cursor.execute('DROP TABLE guildchars_dbchar2')
cursor.execute('DROP TABLE guildchars_dbchar3')
cursor.execute('DROP TABLE guildchars_dbchar4')
cursor.execute('DROP TABLE guildchars_dbchar5')
cursor.execute('DROP TABLE guildchars_dbchar6')
cursor.execute('DROP TABLE guildchars_dbchar7')
cursor.execute('DROP TABLE guildchars_dbchar8')
cursor.execute('DROP TABLE guildchars_dbchar9')
conexion.commit()
