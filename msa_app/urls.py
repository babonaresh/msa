from django.conf.urls import url
from . import views
from django.urls import path, re_path

from django.conf import settings
from django.views.static import serve

app_name = 'msa_app'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),

    url(r'^register/success/$', views.register_success, name='success'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^password/success/$', views.password_success, name='password_success'),

    path('team_list', views.team_list, name='team_list'),

    #path('match_list', views.match_list, name='match_list'),
    path('match_list/<int:pk>', views.match_list, name='match_list'),
    path('match/<int:pk>/', views.match_detail, name='match_detail'),
    path('match/<int:pk>/edit', views.match_edit, name='match_edit'),
    path('match/new', views.match_new, name='match_new'),

    path('team/<int:pk>/edit/', views.team_edit, name='team_edit'),
    path('team/new/', views.team_new, name='team_new'),
    path('team/<int:pk>/delete/', views.team_delete, name='team_delete'),

    path('player_list', views.player_list, name='player_list'),
    path('player_list/<int:pk>/', views.myteamplayer_list, name='myteamplayer_list'),
    path('player/new/', views.player_new, name='player_new'),
    path('player/<int:pk>/', views.player_detail, name='player_detail'),
    path('player/<int:pk>/edit/', views.player_edit, name='player_edit'),
    path('player/<int:pk>/delete/', views.player_delete, name='player_delete'),

    path('assign_role', views.assign_role, name='assign_role'),
    path('roles', views.role_list, name='role_list'),
    path('roles/delete/<int:pk>/', views.delete_role, name='delete_role'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',
            serve, {'document_root': settings.MEDIA_ROOT,})
    ]
