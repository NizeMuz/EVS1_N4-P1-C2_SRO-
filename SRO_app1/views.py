from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Vista(http):
    http="""<h1> Hola, esta es la primera vista </h1>"""
    return HttpResponse(http)