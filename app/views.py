from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mouni(request):
    return HttpResponse('<marquee><h1>helo hi howare you</h1></marquee>')
                        
