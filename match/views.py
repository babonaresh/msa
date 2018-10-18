from django.shortcuts import render
from .models import *
from .forms import *


now = timezone.now()
def home(request):
   return render(request, 'match/home.html',
                 {})

# Create your views here.
