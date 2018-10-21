from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'msa_app'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('team_list', views.team_list, name='team_list'),
    path('matches', views.matches, name='matches'),
    path('team/<int:pk>/edit/', views.team_edit, name='team_edit'),
    path('team/new/', views.team_new, name='team_new'),
]
