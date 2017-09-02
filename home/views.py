from django.shortcuts import render, HttpResponse
from .models import Intro, Team, Contact
# Create your views here.
def index(request):
	intro = Intro.objects.all()
	teams = Team.objects.all()

	return render(request, 'home/index.html', {'intro':intro, 'teams':teams})

def contactSubmit(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		number = request.POST['number']
		subject = request.POST['subject']
		content = request.POST['content']

		Contact.objects.create(
			name = name,
			email = email,
			number = number,
			subject = subject,
			content = content
			)
	return HttpResponse('')







