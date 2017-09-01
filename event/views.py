from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Events
# Create your views here.
class EventListView(ListView):
	model = Events
	context_object_name = 'events'
	template_name = 'event/index.html'
