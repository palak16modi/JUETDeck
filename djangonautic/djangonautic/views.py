#this file will fire the corresponding function when user visits any url
#will send a http response
from django.http import HttpResponse
from django.shortcuts import render  #to return html template

#function for /about..... function name can be anything but call the same name in url
def about(request):
    #return HttpResponse('about')
    return render(request, 'about.html')


def homepage(request):
    #return HttpResponse('homepage')
    return render(request, 'homepage.html')
