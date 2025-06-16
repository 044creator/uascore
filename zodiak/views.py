from django.http import HttpResponse
from django.shortcuts import render

def leo(request):
    return HttpResponse("Zodiak Leo.")

def capricorn(request):
    return HttpResponse("Zodiak Capricorn.")

def scorpio(request):
