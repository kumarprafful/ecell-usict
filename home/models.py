from django.db import models

# Create your models here.
class Intro(models.Model):
	title = models.CharField(max_length=255, default="Intro")
	content = models.TextField()

	def __str__(self):
		return self.title

