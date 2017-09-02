from django.db import models

# Create your models here.
class Intro(models.Model):
	title = models.CharField(max_length=255, default="Intro")
	content = models.TextField()

	def __str__(self):
		return self.title

class Team(models.Model):
	name = models.CharField(max_length=255)
	image = models.ImageField(upload_to='team')
	designation = models.CharField(max_length=1024)

	def __str__(self):
		return self.name + self.designation


class Contact(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	number = models.IntegerField()
	subject = models.CharField(max_length=1024)
	content = models.TextField()

	def __str__(self):
		return self.name + self.subject

