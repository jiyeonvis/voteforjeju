from django.shortcuts import render, redirect
from .models import Candidate, Promise, Press
# Create your views here.
def home(request):
    return render(request, 'home.html')

def gab(request):
    candidates = Candidate.objects.filter(region__iexact='gab')
    return render(request, 'gab.html', {'candi':candidates})

def eul(request):
    candidates = Candidate.objects.filter(region__iexact='eul')
    return render(request, 'eul.html', {'candi':candidates})

def byeong(request):
    candidates = Candidate.objects.filter(region__iexact='byeong')
    return render(request, 'byeong.html', {'candi':candidates})
