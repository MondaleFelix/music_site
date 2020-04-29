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

def album_detail(request, id):
	name = Album.objects.get(id=id)
	print(Song.objects.filter(album=name))


	context = {
		'album': Album.objects.get(id=id),
		"songs_list": Song.objects.filter(album=name)
	}
	return render(request, 'music/album_detail.html',context = context)

def song_detail(request, id):

	context = {
		
		"song": Song.objects.get(id=id)
	}
	return render(request, 'music/song_detail.html',context = context)
