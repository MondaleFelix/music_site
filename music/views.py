from django.http import HttpResponse
from .models import *
from django.shortcuts import render




def home(request):
	return HttpResponse("Hello, world. This is my music site!")

def musicians(request):
	context = {
		'musicians' : Musician.objects.all()
	}
	return render(request, 'music/musician_list.html', context = context)
