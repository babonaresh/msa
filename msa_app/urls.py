from django.conf.urls import url
from . import views
from django.urls import path, re_path


app_name = 'msa_app'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('matches', views.matches, name='matches'),

]