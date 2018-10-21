from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def team_list(request):
    team_list = Team.objects.filter(created_date__lte=timezone.now())
    return render(request, 'custom/team_list.html',
                 {'teams': team_list})
