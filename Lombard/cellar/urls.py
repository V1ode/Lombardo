from django.urls import path
from .views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', index, name='home'),
    path('employees/', employees, name='employees'),
    path('employees/<int:id>/', get_employee, name='get_employee'),
    path('contracts/', contracts, name='contracts'),
    path('get_contract/<int:id>/', get_contract, name='get_contract')
]