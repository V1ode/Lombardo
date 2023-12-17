from django.urls import path
from .views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', index, name='home'),
    path('employees/', employees, name='employees'),
    path('employees/<int:id>/', get_employee, name='get_employee'),
    path('contracts/', contracts, name='contracts'),
    path('contracts/get_contract/<int:id>/', get_contract, name='get_contract'),
    path('tools/', tools, name='tools'),
    path('tools/add_form/', add_form, name='add_form'),
    path('tools/add_form/add_post/', add_post, name='add_post'),
    path('tools/add_form/add_division/', add_division, name='add_division'),
    path('tools/add_form/add_client/', add_client, name='add_client'),
    path('tools/add_form/add_employee/', add_employee, name='add_employee'),
    path('tools/add_form/add_category/', add_category, name='add_category'),
    path('tools/add_form/add_pledged_items_list/', add_pledged_items_list, name='add_pledged_items_list'),
    path('tools/add_form/add_contract/', add_contract, name='add_contract'),
    path('tools/pledged_items/', pledged_items, name='pledged_items'),
    path('tools/pledged_items/search_item/<slug:item>/', search_item, name='search_item'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', login, name='login'),
]