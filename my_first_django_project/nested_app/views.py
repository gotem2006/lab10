from django.shortcuts import render
from django.http import HttpResponse

def nested_view_1(request):
    return HttpResponse("<h1> вложенные маршруты1</h1>")

def nested_view_2(request):
    return HttpResponse("<h1> вложенные маршруты2</h1>")

