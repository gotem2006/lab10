from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.nested_view_1, name='test'),
    path('test2/', views.nested_view_2, name='test2'),
]
