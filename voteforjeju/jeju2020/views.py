from django.shortcuts import render, redirect
from .models import Candidate, Promise, Press
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'jeju2020/home.html')

def gab(request):
    candidates = Candidate.objects.filter(region__iexact='gab')
    
    return render(request, 'jeju2020/gab.html', {'candi':candidates, 'one':0})

def eul(request):
    candidates = Candidate.objects.filter(region__iexact='eul')
    return render(request, 'jeju2020/eul.html', {'candi':candidates})

def byeong(request):
    candidates = Candidate.objects.filter(region__iexact='byeong')
    return render(request, 'jeju2020/byeong.html', {'candi':candidates})

def detail_gab(request, pk):
    candidates = Candidate.objects.filter(region__iexact='gab')
    one_candi = get_object_or_404(Candidate, pk=pk)
    press = Press.objects.filter(candidate=one_candi)
    promise = Promise.objects.get(candidate=one_candi)
    return render(request, 'jeju2020/gab.html', {'candi':candidates, 'one':one_candi, 'press':press, 'promise':promise})
