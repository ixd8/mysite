from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

def index_view(request):
    return HttpResponse('<h1>HomePage</h1>')



def about_view(request):
    return HttpResponse('<h1>AboutPage</h1>')



def contact_view(request):
    return HttpResponse('<h1>ContactPage</h1>')