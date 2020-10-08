
#[VIEWS / Watchlist]
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .services import *


def watchlist(request):
	charlist = Charfullmatrix.objects.all()
	return render(request,'watchlist.html',
	{'charlist':charlist})

#webkey se esta usando para el analyzer
def webkey(request):
	if request.method == 'POST':
		key = request.POST['webkeywatch']
		if key == "magumbo":
			print("Key correcta")
			clockapi()
			return redirect ('watchlist')
		else:
			print("Key incorrecta")
			return redirect ('watchlist')


def vista_clearallreg(request):
	#url [clearallreg/]
	clearallreg()
	return HttpResponse('Tablas de matrix borradas')
