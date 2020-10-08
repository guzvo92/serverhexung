
#[SERVICES / GUILDBOARD]

################################     CONSTRUCTORES      #######################################
import requests
from .services_filemakers import *


sizelist = 100
creandofilemodelos(sizelist,"appmain3guildboard/auto_models.py") #crea archivo de MODELOS
creandoautofile(sizelist,"appmain3guildboard/auto_file.py") #me crea los N modelos finales

print("\n")

############################## EMPIEZAN Services del componente ##################################
from .auto_models import *
from .auto_file import *
from .services_singles import *
from .models import *

#[X3] #ALONE // Creacion de matrices HG1x y HG2x
#proceso existente debido al limite de 100 registroscope HG2
def writeallcharsguild():
    #contexto de esas matrices usados en guildclockapi
    global HG1x
    HG1x = []
    global HG2x
    HG2x = []
    count= 0

    #HG1 NO SE USA
    #Allcharsguild siempre tiene el numero exacto de chars
    #porque el requestguild siempre la borra
    chars = Allcharsguild.objects.all()

    for x in chars:
        HG1x.append(x) ############## TARGET
        count += 1
    HG2x = HG2[:count] #lista[inicio:fin] // Truncar lista
    #Recordar que HG1x es una matriz de Objetos
    #Recordar que HG2x es una matriz de nombres

    print("[X3/data] - " + str(len(HG1x)) + " chars en guild")
    print("---------------------------------------")
    print("Matrices del render HG1x Y HG2x creadas")
    print("\n")


#[X4]
#con 56chars me mamo 80mbs
def guildclockapi():
    #hace los request,los carga en HG1, los filtra en HG1x,
    #hace las N peticiones deacuerdo a HG1x y los salva en N Dbs

    requestguild('Imperio Mexicano') #[ISOLATED] request
    #me traigo el charnumber de el ultimo registro realizado
    # Importante--- despues de hacer el request
    scopedmat_last = Scopedmatrix.objects.last()
    lastnum_scopedmat = int(scopedmat_last.mcharcounter)
    countup = 0
    loadingpercent_one = 100/lastnum_scopedmat

    writeallcharsguild()  #[ISOLATED] creacion de matrices HG1x y HG2x

    for x in range (lastnum_scopedmat) :
    #hace los registros uno a uno en las db
        requestchar(HG1x[x].name,HG2x[x])
        #Recordar que HG1x es una matriz de Objetos con atributos
        #Recordar que HG2x es una matriz de nombres de DBs

        countup += 1
        loading = int(countup*loadingpercent_one)

        out1 = "[Request] - " + str(countup) +" de " + str(lastnum_scopedmat)
        out2 = " Loading ... (" + str(loading) + "%)"
        estadofinal = out1 + out2
        print (estadofinal)

#analyzer no ocupa internet revisa los registros ya hechos
def analyzer():
    Renderguildmatrix.objects.all().delete()
    scopedmat_last = Scopedmatrix.objects.last()
    lastnum_scopedmat = int(scopedmat_last.mcharcounter)
    for x in range(lastnum_scopedmat):
        lvlayzer(HG2[x],x) # el analyzer es hacia una DB
