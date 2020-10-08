import os #para crear el salto de linea

#############################    funciones file makers  ########################################
#para una estructura de 50 registros

def paracursores(num,uri):

    file = open(uri, "w") #limpiando archivo
    file.write("" + os.linesep)
    file.close()  #limpiando archivo

    file = open(uri, "a")
    file.write("import sqlite3" + os.linesep)
    file.write("conexion = sqlite3.connect('../db.sqlite3')" + os.linesep)
    file.write("cursor = conexion.cursor()" + os.linesep)
    file.write("\n")

    line0 = "cursor.execute('DROP TABLE guildchars_dbchar"
    line1 = "')"

    for x in range(num):
        file.write(line0 + str(x)+ line1 + os.linesep)

    file.write("conexion.commit()" + os.linesep)
    file.close()



def paradbbrowser(num,uri):

    file = open(uri, "w") #limpiando archivo
    file.write("" + os.linesep)
    file.close()  #limpiando archivo

    file = open(uri, "a")
    line0 = "DROP TABLE IF EXISTS guildchars_dbchar"
    line1 = ";"
    for x in range(num):
        file.write(line0 + str(x)+ line1 + os.linesep)

    file.close()

#paracursores(10,"auto_droptables.py")
paradbbrowser(100,"auto_droptables.sql")
