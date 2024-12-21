from django.shortcuts import render
from django.http import HttpResponse


#Часть 2-1
def hello_world1(request):
    return HttpResponse("<h1>Hello, World!</h1>")
#Часть 2-2
#Обработка параметров запроса
def hello_world2(request, name):
    return HttpResponse(f"<h1>Hello, {name}!</h1>")
#Часть 2-3
#Получение данных из строки запроса
def hello_world3(request, name,age):
    age = request.GET.get('age', 'unknown')
    return HttpResponse(f"<h1>Hello, {name}! You are {age} years old.</h1>")
#Часть 2-4
from django.shortcuts import redirect

def redirect_example(request):
    return redirect('hello_world', name='Гость')
#Часть 2-5
from django.http import JsonResponse

def json_example(request):
    data = {"name": "Viktor", "age": 22}
    return JsonResponse(data)
#Часть 2-6
def hello_world6(request, name):
    response = HttpResponse(f"<h1>Hello, {name}!</h1>")
    response.set_cookie('username', name)
    return response
def show_cookies(request):
    cookies = request.COOKIES
    return HttpResponse(f"<h1>Cookies: {cookies}</h1>")
