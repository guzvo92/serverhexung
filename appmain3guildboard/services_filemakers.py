import os #para crear el salto de linea


#############################    funciones file makers  ########################################
#para una estructura de 50 registros

def creandofilemodelos(num,uri):

    file = open(uri, "w") #limpiando archivo
    file.write("" + os.linesep)
    file.close()  #limpiando archivo

    contentimports = "from django.db import models"
    contentimports2 = "from django.utils.timezone import now"
    contentline0 = "class Dbchar"
    contentline1 = "(models.Model):"
    contentline2 = "name = models.CharField(max_length=50)"
    contentline3 = "vocation= models.CharField(max_length=50)"
    contentline4 = "level= models.CharField(max_length=50)"
    contentline5 = "lastlog= models.CharField(max_length=50)"
    contentline6 = "created_at= models.DateTimeField(auto_now_add=True)"

    file = open(uri, "a")
    file.write("" +  contentimports + "" + os.linesep)
    file.write("" +  contentimports2 + "" + os.linesep)
    file.write("\n")

    for x in range(num):

        file.write("" +  contentline0 + "" + str(x))
        file.write("" +  contentline1 + "" + os.linesep)
        file.write("" + "\t"+  contentline2 + "" + os.linesep)
        file.write("" + "\t"+ contentline3 + "" + os.linesep)
        file.write("" + "\t"+ contentline4 + "" + os.linesep)
        file.write("" + "\t"+ contentline5 + "" + os.linesep)
        file.write("" + "\t"+ contentline6 + "" + os.linesep)
        file.write("\n")

    file.close()


def creandoautofile(num,uri):

    file = open(uri, "w") #limpiando archivo
    file.write("" + os.linesep)
    file.close()  #limpiando archivo

    file = open(uri, "a")
    file.write( "from .auto_models import *" + os.linesep)
    file.write( "\n" ) ###########################3###################

    #Crea matriz HG1/CHARS
    file.write( "HG1=[" )
    for x in range(num):
        dburi = ("char"+str(x))
        file.write("'")
        file.write(dburi)
        file.write("'")
        file.write(",")
    file.write(  "]" + os.linesep)

    file.write( "\n" ) ###########################3###################

    #Crea matriz HG2/MODELS
    file.write( "HG2=[" )
    for x in range(num):
        dburi = "Dbchar"+str(x)
        file.write(dburi)
        file.write(",")
    file.write(  "]" + os.linesep)

    file.write( "\n" ) ###########################3###################

    #crea funcion de borrado de registros de tamaño N
    file.write( "def clearallreg():" + os.linesep)
    for x in range(num):
        file.write( "\t")
        dburi = "Dbchar"+str(x)
        file.write(dburi + ".objects.all().delete()"+ os.linesep)

    file.close()  #limpiando archivo
