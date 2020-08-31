from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def date_time_view(request):
    date=datetime.datetime.now()
    return HttpResponse("<h1 style='color:blue'>Current date and time at server is: "+str(date)+"</h1>")
