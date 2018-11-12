from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

now = timezone.now()
def home(request):
   return render(request, 'base/home.html',
                 {'base': home})

def match_list(request):
    matches_sch = Match.objects.filter(match_status='scheduled')
    matches_full = Match.objects.filter(match_status='full_time')
    matches_all = Match.objects.filter(created_date__lte=timezone.now())
    return render(request, 'custom/match_list.html', {'matches_sch': matches_sch,
                                                   'matches_full': matches_full,
                                                   'matches_all': matches_all})

@login_required
def match_detail(request, pk):
    match = get_object_or_404(Match, pk=pk)
    home_team = match.home_team
    guest_team = match.guest_team
    return render(request, 'custom/match_detail.html', {'match': match,
                                                'home_team': home_team,
                                                'guest_team': guest_team})

# Create your views here.
@login_required
def team_edit(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == "POST":
        #update
        form = TeamForm(request.POST,instance=team)
        if form.is_valid():
            team = form.save(commit=False)
            team.updated_date = timezone.now()
            team.save()
            teams = Team.objects.filter(created_date__lte=timezone.now())
            return render(request, 'custom/team_list.html', {'team_list': teams})
    else:
        # edit
        form = TeamForm(instance = team)
    return render(request, 'custom/team_edit.html', {'form': form})

@login_required
def team_new(request):
    if request.method == "POST":
        #update
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.created_date = timezone.now()
            team.save()
            teams = Team.objects.filter(created_date__lte=timezone.now())
            return render(request, 'custom/team_list.html', {'team_list': teams})
    else:
        # edit
        form = TeamForm()
    return render(request, 'custom/team_edit.html', {'form': form})

def team_list(request):
    team_list = Team.objects.filter(created_date__lte=timezone.now())
    return render(request, 'custom/team_list.html',
                 {'team_list': team_list})

@login_required

def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    team.delete()
    return redirect('msa_app:team_list')