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

#PARTY_CHOICES = ( ('jhd', 'jhd'), ('dmj', 'dmj'), ('jed', 'jed'), )
def candi(candidate): 
    """return party, partyback, partynamec, partyfontc"""
    if candidate.party == 'jhd':
        return "자유한국당", "red", "grey", "white"
    elif candidate.party == 'dmj':
        return "더불어민주당", "rgb(41, 24, 217)","grey", "white"
    elif candidate.party == 'jed':
        return "정의당", "yellow","grey", "black"
    else :
        return "아몰랑", "black","grey", "white"

def detail_gab(request, pk):
    candidates = Candidate.objects.filter(region__iexact='gab')
    one_candi = get_object_or_404(Candidate, pk=pk)
    party, partyback, partynamec, partyfontc = candi(one_candi)
    press = Press.objects.filter(candidate=one_candi)
    promise = Promise.objects.get(candidate=one_candi)
    return render(request, 'jeju2020/gab.html', {'candi':candidates, 'one':one_candi, 'press':press, 'promise':promise, 'party':party, 'partyback':partyback, 'partynamec':partynamec, 'partyfontc':partyfontc})

def detail_eul(request, pk):
    candidates = Candidate.objects.filter(region__iexact='gab')
    one_candi = get_object_or_404(Candidate, pk=pk)
    party, partyback, partynamec, partyfontc = candi(one_candi)
    press = Press.objects.filter(candidate=one_candi)
    promise = Promise.objects.get(candidate=one_candi)
    return render(request, 'jeju2020/gab.html', {'candi':candidates, 'one':one_candi, 'press':press, 'promise':promise, 'party':party, 'partyback':partyback, 'partynamec':partynamec, 'partyfontc':partyfontc})

def detail_byeong(request, pk):
    candidates = Candidate.objects.filter(region__iexact='gab')
    one_candi = get_object_or_404(Candidate, pk=pk)
    party, partyback, partynamec, partyfontc = candi(one_candi)
    press = Press.objects.filter(candidate=one_candi)
    promise = Promise.objects.get(candidate=one_candi)
    return render(request, 'jeju2020/gab.html', {'candi':candidates, 'one':one_candi, 'press':press, 'promise':promise, 'party':party, 'partyback':partyback, 'partynamec':partynamec, 'partyfontc':partyfontc})


def birye(request):
    return render(request, 'jeju2020/birye.html')