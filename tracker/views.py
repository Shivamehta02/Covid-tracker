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
    
def hospital(request):
    
    info = requests.get('https://api.rootnet.in/covid19-in/hospitals/beds')
    total = info.json()['data']['summary']
    regional= info.json()['data']['regional']
    
    print(total)
    return render(request,"tracker/hospital.html",{
        'total':total,
        'states':regional
    })
    