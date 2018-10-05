from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('msa/', include('msa.urls', namespace='msa')),
    path('match/', include('match.urls', namespace='match')),
]
