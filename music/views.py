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


def musician_detail(request, id):
	name = Musician.objects.get(id=id)

	context = {
		'musician': Musician.objects.get(id=id),
		"albums_list": Album.objects.filter(artist=name)
	}
	return render(request, 'music/musician_detail.html',context = context)
