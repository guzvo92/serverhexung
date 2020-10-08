from django.shortcuts import render, HttpResponse, redirect
from .services import *
#guildboard VIEWS
'''
A ESTA APLICACION LE QUEDA PENDIENTE LOS METODOS PARA
RENDERIZAR EL TIEMPO PENDIDENTE EN LA VISTA PORQUE SON 2TRIGGERS
1/ guildclockapi()
2/ analyzer() - no ocupa internet
'''

#solo renderiza la pagina con los registros
def guildboard(request):
    charlist = Renderguildmatrix.objects.all()
    return render(request,'guildboard.html',
        {'charlist':charlist})

#webkey se esta usando para el runrequest
def runrequest(request):
    if request.method == 'POST':
        key = request.POST['keyrequest']
        if key == "magumbo":
            print("Key correcta")
            guildclockapi()
            return redirect ('guildboard')

        else:
            print("Key incorrecta")
            return redirect ('guildboard')


#webkey se esta usando para el analyzer
def runanalyzer(request):
    if request.method == 'POST':
        key = request.POST['keyanalyzer']
        if key == "magumbo":
            print("Key correcta")
            analyzer()
            return redirect ('guildboard')

        else:
            print("Key incorrecta")
            return redirect ('guildboard')
