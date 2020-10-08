from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *

def mysteries(request):
	misterios= Mystery.objects.all()
	return render (request, 'mystery_board.html',
	{'misterios':misterios})

def clear(request,id):
	misterio = Mystery.objects.get(pk=id)
	misterio.delete()
	return redirect('admingen')

def save_mystery(request):
	if request.method == 'POST':
		titlez =request.POST['title']
		contentz = request.POST['content']
		mystery = Mystery(
			title = titlez,
			content = contentz,)

		mystery.save()
		return redirect('admingen')
