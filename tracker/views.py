from django.shortcuts import render
from django.http import HttpResponse 
import requests
# Create your views here.

def home(request):
    
    result = requests.get('https://api.rootnet.in/covid19-in/stats/latest')
    summary = result.json()['data']['unofficial-summary']
    states= result.json()['data']['regional']
    
   
    return render(request,"tracker/index.html",{
        'summary':summary,
        'states':states
    })
    