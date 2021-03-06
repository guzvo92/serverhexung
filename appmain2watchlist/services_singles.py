import requests
from .models import *
from datetime import datetime, timedelta

global requestguild_charcounter
global requestguild_guild

global helion
helion = "Stringify"

#################### fetch master ####################################
#importante si quieres sacar una variable de una funcion
#ponle al final de la funcion el return de la variable
# En tu otro archivo llamala y encierrala en otr variable

#[FUNG #1] ALONE
def requestinfochar(namechar):
    urlini = 'https://api.tibiadata.com/v2/characters/'
    urlend = '.json'
    searchar =urlini+namechar+urlend

    response = requests.get(searchar)
    if response.status_code == 200:
        resdi = response.json()
        ReqRes = resdi.get('characters')
        #print(user.get('name'))
        namex = ReqRes.get('data').get('name')
        vocationx = ReqRes.get('data').get('vocation')
        levelx = ReqRes.get('data').get('level')
        lastx = ReqRes.get('data').get('last_login')[0].get('date')

        #datachar = {'name' : namex , 'lvl': ['Django','JavaScript'] }
        datachar = {
        'name' :     namex ,
        'vocation':  vocationx,
        'level':       levelx,
        'last':      lastx
        }

        return datachar

"""----------------------------------------------------------------------------------------"""

#[FUNG #2] ALONE
#Request multiple a tibia.com y guarda en db
#se hizo asi para poder tener una funcion de peticion y una de registro
def requestchar(char,modelo):
    urlini = 'https://api.tibiadata.com/v2/characters/'
    urlend = '.json'
    url = urlini + char + urlend

    response = requests.get(url)

    if response.status_code == 200:
        resdi = response.json()
        ReqRes = resdi.get('characters')
        #print(user.get('name'))

        namex = ReqRes.get('data').get('name')
        vocationx = ReqRes.get('data').get('vocation')
        levelx = ReqRes.get('data').get('level')
        lastx = ReqRes.get('data').get('last_login')[0].get('date')

        #guardando data
        registro = modelo(
    			name = namex,
    			vocation = vocationx,
    			level = levelx,
    			lastlog = lastx)
        registro.save()

"""----------------------------------------------------------------------------------------"""
#[FUNG #4] ISOLATED  (outputDB [Analyzer] = Renderguildmatrix)
#Esta funcion se tarda porque tambien hace un request en el lvlnow
#Esta funcion forma la render guild matrix
def lvlayzer(modelocharsel):

    #saco la hora actual y creo variables para -1dia/-1week/-1month
    tiemponow = (datetime.today()).strftime("%Y-%m-%d %H:%M")
    #print datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] #output// 2020-05-04 10:18:32.926
    lastday = (datetime.today() - timedelta(hours=24)).strftime("%Y-%m-%d %H:%M")
    lastweek = (datetime.today() - timedelta(days=7)).strftime("%Y-%m-%d %H:%M")
    lastmonth = (datetime.today() - timedelta(days=30)).strftime("%Y-%m-%d %H:%M")

    # todo metodo que use el orm con OBJECTS.FILTER te genera el objeto QUERYSET
    QuerySetTimeday = modelocharsel.objects.filter(created_at__range=[lastday,tiemponow])
    QuerySetTimeweek = modelocharsel.objects.filter(created_at__range=[lastweek,tiemponow])
    QuerySetTimemonth = modelocharsel.objects.filter(created_at__range=[lastmonth,tiemponow])

    querylastday = []   #[Q1]
    querylastweek = []  #[Q2]
    querylastmonth = [] #[Q3]

    #ERROR del min(arg) es en las variables de abajo no en estos querys
    #Si no hay objetos simplemente te regresa el Query [Q1/Q2/Q3] VACIOS

    # -------------------------------------------- manejando el dia
        #De los objetos entre ayer y hoy recorrelos
        #Saca el lvl Y AÑADELOS en querylastday
    for y in QuerySetTimeday:
        querylastday.append(y.level)
    try:
        #Saca el menor y el mayor/ Haz la diferenecia
        lvllastday = int(min(querylastday))
        lvltoday = int(max(querylastday))
        lvlday = lvltoday-lvllastday
    except:
        lvlday = 0
        print("No hay objetos en ultimas 24h")

    # -------------------------------------------- manejando la semana

    for y in QuerySetTimeweek:
        querylastweek.append(y.level)
    try:
        lvliniweek = int(min(querylastweek))
        lvlfinweek = int(max(querylastweek))
        lvlweek = lvlfinweek-lvliniweek
        #print(lvlweek)
    except:
        lvlweek = 0;
        print("No hay objetos en la ultima semana")

    # -------------------------------------------- manejando el mes

    for y in QuerySetTimemonth:
        querylastmonth.append(y.level)
    try:
        lvlini = int(min(querylastmonth))
        lvlfin = int(max(querylastmonth))
        lvlmonth = lvlfin-lvlini
        #print(lvlmonth)
    except:
        lvlmonth = 0
        print("No hay objetos en el ultimo mes")

    query = modelocharsel.objects.all()
    #printeando un atributo de una lista de un listado de objetos
    namex = query[0].name
    vocationx = query[0].vocation

    #modelocharsel = es 1 valor(conjunto de objetos) del listado de DBs de HG2
    #se embebe listado de objetos en una variable "query"
    #query[0].name = del listado de objetos de modelocharsel es el name del primer objeto[0]
    #print("[Analyzer] - " + "{" + str(query[0].name) + "} - " + str(lvliniweek) + "/" + str(lvlfinweek))

    #char sacado del query de los objects
    #este mini request es para en el render sacar el lvl actual
    try: #por si no hay internet
        importe_datachar = requestinfochar(namex)
    except:
        importe_datachar = {'name' : "nada" , 'level': 0 }
        print("[Exception handle] - lvlnow desconocido no hay internet")
    #quieres sacarlos de un return tienes que llamarlos como aqui

    #NO HAY FOR porque toda la funcion es para 1DB/1CHAR
    registrox = Charfullmatrix(
			name = namex,
			vocation = vocationx,
			levelnow = importe_datachar['level'],
			levelday = lvlday,
            levelweek = lvlweek,
            levelmonth = lvlmonth,
            lastupdate = tiemponow)
    registrox.save()
    #este return es solo par aejemplificar como se extraen
    #de esta funcion hacia el server
    #return lvlday,lvlweek,lvlmonth #me retorna una tupla

"""----------------------------------------------------------------------------------------"""

#G4
def clearallreg():
    CharegB1.objects.all().delete()
    CharegB2.objects.all().delete()
    CharegB3.objects.all().delete()
    CharegB4.objects.all().delete()
    CharegB5.objects.all().delete()
    CharegB6.objects.all().delete()
    CharegB7.objects.all().delete()
    CharegB8.objects.all().delete()
    CharegB9.objects.all().delete()
    Charfullmatrix.objects.all().delete()
