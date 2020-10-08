import requests
from .models import *
from .services_singles import *

##############################################################################
#G5
def examapleloadcharmatrixdata():
    dataload = []

    chars = Charmatrix.objects.all()
    count= 0
    for x in chars:
        #dataload.insert(count,x.name)
        dataload.append(x.name)
        #data.insert(count,x)-- para diccionarios
        #data.update(count,x)
        count += 1
    print("dataload -> " + str(dataload))
    data.update(dataload)
    print("data -> " + str(data))
    #funcionan pero update me agrega elemento 0 en blanco

#diccionario['cursos'][0]#Python /accediendo a un objeto de lista dentro de otra
#set conjunto de datos no ordenado no puede iterarse
#lista conjunto ordenado por un index
#diccionario conjunto sin orden pero con keys
#data = {'','','','','','','','',''} #este es un set
#datax = ['0','1','2','3','4','5','6','7','8'] #esta es una lista

data = ['0','1','2','3','4','5','6','7','8'] #esta es una lista

#charB1=data[0] #para listas
#charB2= data.get(1) #para diccionarios
#HG1 = [charB1,charB2,charB3,charB4,charB5,charB6,charB7,charB8,charB9]
HG2 = [CharegB1,CharegB2,CharegB3,CharegB4,CharegB5,CharegB6,CharegB7,CharegB8,CharegB9]

#G7
#corre funcion que hace el listado HG1 (data) proveniente
#de DB Charmatrixdata
# HG1 = listado de charnames
# HG2 = listado de DBs
def clockapi():
    Charfullmatrix.objects.all().delete()
    count= 0

    #loadcharmatrixdata exfunction
    chars = Charsadminwatchlist.objects.all()
    for x in chars:
        data[count] = x.name
        #data.append(x.name)
        count += 1
    print("[G6/data] - " + str(data))

    #carga los nombres guardados en DB Charsadminwatchlist
    #y los acomoda en Listado data sobreescribiendo lo existente

    HG1 = [data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8]]
    requestchar(HG1[0],HG2[0])
    requestchar(HG1[1],HG2[1])
    requestchar(HG1[2],HG2[2])
    requestchar(HG1[3],HG2[3])
    requestchar(HG1[4],HG2[4])
    requestchar(HG1[5],HG2[5])
    requestchar(HG1[6],HG2[6])
    requestchar(HG1[7],HG2[7])
    requestchar(HG1[8],HG2[8])
    print('[G7] - Registros JSON api plasmados en serverdb')

    for x in HG2:
        query = x.objects.all()
        lvlayzer(x)

#funcion se tarda 16seg en
#1 - crear los Registros (10s)
#2 - crear variables y guardar en Charfullmat objs (6s)
