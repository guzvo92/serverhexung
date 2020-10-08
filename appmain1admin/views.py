
#[VIEWS / appmain1admin]

from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.

def index(request): return render(request,'1_index.html')

from appmain2watchlist.models import Charsadminwatchlist
from appmain2watchlist.forms import FormCharmatrix
from appmain4mysteries.forms import FormMystery
from appmain4mysteries.models import Mystery

def admingen(request):
	data = ['0','1','2','3','4','5','6','7','8'] #esta es una lista
	
	formulario_mystery = FormMystery()
	formulario_charmat = FormCharmatrix()
	misterios= Mystery.objects.all()
	matrixchars= Charsadminwatchlist.objects.all()
	count= 0
	#loadcharmatrixdata exfunction
	chars = Charsadminwatchlist.objects.all()
	for x in chars:
		data[count] = x.name
		#data.append(x.name)
		count += 1
	print("[G6/data] - " + str(data))

	return render (request, '0_admingen.html',
	{
	'misterios':misterios,
	'form_mystery':formulario_mystery,
	'form_chars':formulario_charmat,
	'charsmatrix':matrixchars,
	})

def clearchar(request,id):
	char = Charsadminwatchlist.objects.get(pk=id)
	char.delete()
	return redirect('admingen')

def save_metcharinmatrix(request):
	if request.method == 'POST':
		namechar =request.POST['name']
		char = Charsadminwatchlist(
			name = namechar
			)

		char.save()
		return redirect('admingen')
