from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

now = timezone.now()
def home(request):
   return render(request, 'base/home.html',
                 {'base': home})

def matches(request):
    matches_sch = Match.objects.filter(match_status='scheduled')
    matches_full = Match.objects.filter(match_status='full_time')
    matches_all = Match.objects.filter(created_date=timezone.now())
    return render(request, 'custom/matches.html', {'matches_sch': matches_sch,
                                                   'matches_full': matches_full,
                                                   'matches_all': matches_all})
# Create your views here.


def team_edit(request,pk):
    team = get_object_or_404(Team,pk=pk)
    if request.method == "POST":
        #update
        form = Team(request.POST,instance=team)

    if form.is_valid():
        team = form.save(commit=False)
        team.update_date = timezone.now()
        team.save()
        team = Team.objects.filter(create_date_lte=timezone.now())
        return render(request, 'custom/team_edit.html', {'team': team})

    else:
        # edit
        form = Team(instance = team)
    return render(request, 'msa/team_edit.html', {'form': form})

@login_required
def team_list(request):
    team_list = Team.objects.filter(created_date__lte=timezone.now())
    return render(request, 'custom/team_list.html',
                 {'teams': team_list})
