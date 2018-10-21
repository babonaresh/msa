from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *



now = timezone.now()
def home(request):
   return render(request, 'base/home.html',
                 {'base': home})

def matches(request):
    matches = Match.objects.filter(created_date__lte=timezone.now())
    return render(request, 'custom/matches.html', {'match': matches})
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



