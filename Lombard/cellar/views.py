from django.core.exceptions import PermissionDenied
from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseServerError, \
    HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from cellar.models import *


data = {
    'index': {
        'title': 'Главная',
    },
    'employees': {
        'title': 'Сотрудники',
        'info': Employees.objects.all(),
    },
    'get_employee': {
        'title': 'Федор Михайлов',
        'info': Employees.objects.get(Employee_id=1),
        'post': 'post',
        'division': 'division',

    },
    'clients': {
        'title': 'Клиенты',
    },
}


def index(request):
    return render(request, 'Lombard/index.html', context=data['index'])


def employees(request):
    return render(request, 'Lombard/employees.html', context=data['employees'])


def get_employee(request, id):
    if not (id > 0 and id < 8): # ?When id is negative its not working
        return HttpResponse('<div style="height: 18vh; background: #ffc"> <br><br> <h1 style="text-align: center"> Сотрудника с таким id не существует </h1> </div>')


    info = Employees.objects.get(Employee_id=id)
    data['get_employee']['info'] = info

    data['get_employee']['title'] = info.First_name + ' ' + info.Last_name

    post = info.Post_id
    data['get_employee']['post'] = post

    division = info.Division_id
    data['get_employee']['division'] = division
    return render(request, 'Lombard/get_employee.html', context=data['get_employee'])


def clients(request):
    return render(request, 'Lombard/clients.html', context=data['clients'])


def check(request):
    return


def bad_request(request, exception):
    return HttpResponseBadRequest('<h1> Мы не поняли ваш запрос <h1>')


def forbidden(request, exception):
    return HttpResponseForbidden('<h1> Доступ ЗАПРЕЩЕН <h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена. Проверьте адрес!!! </h1>')


def server_down(exception):
    return HttpResponseServerError('<h1> Сервер себя плохо чувствует. Страница недоступна <h1>')
