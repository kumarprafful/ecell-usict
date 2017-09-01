from django.conf.urls import url
from .views import EventListView

app_name = 'event'


urlpatterns = [
	url(r'^$', EventListView.as_view(), name='index')

]