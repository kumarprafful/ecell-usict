from django.shortcuts import render
from .models import Intro
# Create your views here.
def index(request):
	intro = Intro.objects.all()
	return render(request, 'home/index.html', {'intro':intro})
