from django.db import models

# Create your models here.

class Musician(models.Model):
	name = models.CharField(max_length=50)

	# Makes it more human readable
	def __str__(self):
		return self.name

class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, null=True)
    genre = models.CharField(max_length=50, null=True)
    publish_date = models.DateField(blank=True, null=True)

    def __str__(self):
      return self.name


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    num_stars = models.IntegerField()
    length = models.IntegerField()

    def __str__(self):
        return self.name
