from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'match'
urlpatterns = [

    path('', views.home, name='home'),
]
