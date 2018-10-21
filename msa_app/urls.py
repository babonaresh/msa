from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'msa_app'
urlpatterns = [

    path('team_list', views.team_list, name='team_list'),

]
