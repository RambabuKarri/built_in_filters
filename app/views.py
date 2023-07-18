from django.shortcuts import render
import datetime

# Create your views here.
def built_in_filters(request):
    
    d={'data':'Hi, Im Groot, love you 3000'}
    return render(request,'built_in_filters.html',d)


