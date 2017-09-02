from django.contrib import admin
from .models import Intro, Team, Contact

# Register your models here.

admin.site.register(Intro)
admin.site. register(Team, list_display=['name','designation'])
admin.site.register(Contact)