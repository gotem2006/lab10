from django.urls import path
from .views import hello_world1, hello_world2, hello_world3,redirect_example,json_example,show_cookies,hello_world6

urlpatterns = [
    path('', hello_world1, name='hello_world'),
    path('hello/<str:name>/', hello_world2, name='hello_world'),
    path('hello/<str:name>/<str:age>/', hello_world3, name='hello_world'),
    path('redirect/', redirect_example, name='redirect_example'),
    path('json/', json_example, name='VItek'),
    path('cookies/', show_cookies, name='show_cookies'),
    path('hello6/<str:name>/', hello_world6, name='hello_world'),


]
