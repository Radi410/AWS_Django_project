from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#example view
def home(request):
    return HttpResponse("Velkommen til hjemmesiden!")   


    