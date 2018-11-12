from django.conf.urls import url
from . import views
from django.urls import path, re_path

from django.conf import settings
from django.views.static import serve

app_name = 'msa_app'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('team_list', views.team_list, name='team_list'),
    path('match_list', views.match_list, name='match_list'),
    path('match/<int:pk>/', views.match_detail, name='match_detail'),
    path('team/<int:pk>/edit/', views.team_edit, name='team_edit'),
    path('team/new/', views.team_new, name='team_new'),
    path('team/<int:pk>/delete/', views.team_delete, name='team_delete'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',
            serve, {'document_root': settings.MEDIA_ROOT,})
    ]
