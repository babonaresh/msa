from django.shortcuts import render
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
