from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseServerError, \
    HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from cellar.models import *
from .forms import *


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
    'contracts': {
        'title': 'Контракты',
        'info': Contracts.objects.all(),
    },
    'get_contract': {
        'title': 'Контракт №1',
        'info': 'info',
        'employee': Employees.objects.get(Employee_id=1),
        'pledged_items_list': Pledged_items_list.objects.get(Pledged_items_list_id=1),
        'category': 'category',
        'client': Clients.objects.get(Client_id=1),
        'items': Pledged_items_list.objects.all(),
        'translation' : {
            'Машина': 'car',
            'Алмаз': 'diamond',
            'Зачетка': 'gradebook',
            'Пачка бумаги': 'paper',
        },
    },
    'tools': {
        'title': 'Инструменты',
    },
    'pledged_items': {
        'title': 'Заложенные вещей',
        'items': Pledged_items_list.objects.all(),
        'find': [
            'Машина',
            'Алмаз',
            'Зачетка',
            'Пачка бумаги',
        ],
        'translation' : {
            'Машина': 'car',
            'Алмаз': 'diamond',
            'Зачетка': 'gradebook',
            'Пачка бумаги': 'paper',
        },
    },
    'search_item': {
        'title': 'Поиск вещи',
        'item': 'item',
    },
    'add_form': {
        'title': 'Добавить форму',
    },
    'add_post': {
        'title': 'Добавить должность',
        'func': 'func',
    },
    'add_division': {
        'title': 'Добавить подразделение',
        'func': 'func',
    },
    'add_client': {
        'title': 'Добавить клиента',
        'func': 'func',
    },
    'add_employee': {
        'title': 'Добавить сотрудника',
        'func': 'func',
    },
    'add_category': {
        'title': 'Добавить категорию',
        'func': 'func',
    },
    'add_pledged_items_list': {
        'title': 'Добавить заложенную вещь',
        'func': 'func',
    },
    'add_contract': {
        'title': 'Добавить контракт',
        'func': 'func',
    },
}


def login(request):
    return render(request, 'Lombard/login.html')


def index(request):
    return render(request, 'Lombard/index.html', context=data['index'])


def employees(request):
    data['employees']['info'] = Employees.objects.all()

    return render(request, 'Lombard/employees.html', context=data['employees'])


def get_employee(request, id):
    max_id = Employees.objects.all().count()

    if not (id > 0 and id <= max_id): # ?When id is negative its not working
        raise ValueError('Сотрудника с таким именем не существует')
        # return HttpResponse('<div style="height: 18vh; background: #ffc"> <br><br> <h1 style="text-align: center"> Сотрудника с таким id не существует </h1> </div>')

    info = Employees.objects.get(Employee_id=id)
    data['get_employee']['info'] = info

    data['get_employee']['title'] = info.First_name + ' ' + info.Last_name

    post = info.Post_id
    data['get_employee']['post'] = post

    division = info.Division_id
    data['get_employee']['division'] = division
    return render(request, 'Lombard/get_employee.html', context=data['get_employee'])


def contracts(request):
    data['contracts']['info'] = Contracts.objects.all()

    return render(request, 'Lombard/contracts.html', context=data['contracts'])


def get_contract(request, id):
    max_id = Contracts.objects.all().count()

    if not (id > 0 and id <= max_id):
        raise ValueError('Такого контракта не существует')

    data['get_contract']['title'] = f"Контракт №{id}"

    info = Contracts.objects.get(Contract_id=id)
    data['get_contract']['info'] = info

    employee = info.Employee_id
    data['get_contract']['employee'] = employee

    pledged_items_list = info.Pledged_items_list_id
    data['get_contract']['pledged_items_list'] = pledged_items_list

    category = pledged_items_list.Category_id
    data['get_contract']['category'] = category

    client = info.Client_id
    data['get_contract']['client'] = client

    return render(request, 'Lombard/get_contract.html', context=data['get_contract'])


def tools(request):
    return render(request, 'Lombard/tools.html', context=data['tools'])

def add_form(request):
    return render(request, 'Lombard/add_form.html', context=data['add_form'])


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        data['add_post']['func'] = PostForm()
    return render(request, 'Lombard/add_post.html', context=data['add_post'])


def add_division(request):
    if request.method == "POST":
        form = DivisionForm(request.POST)

        if form.is_valid():
            division = form.save(commit=False)
            division.save()
    else:
        data['add_division']['func'] = DivisionForm()
    return render(request, 'Lombard/add_division.html', context=data['add_division'])


def add_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)

        if form.is_valid():
            client = form.save(commit=False)
            client.save()
    else:
        data['add_client']['func'] = ClientForm()
    return render(request, 'Lombard/add_client.html', context=data['add_client'])


def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)

        if form.is_valid():
            if int(request.POST['Employee_id']) == int(Employees.objects.all().count()+1):
                employee = form.save(commit=False)
                employee.save()
            else:
                raise ValueError(f"Указан неверный ИД")
        else:
            raise ValueError('Данные введены неверно')
    else:
        data['add_employee']['func'] = EmployeeForm()
    return render(request, 'Lombard/add_employee.html', context=data['add_employee'])


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.save()
    else:
        data['add_category']['func'] = CategoryForm()
    return render(request, 'Lombard/add_category.html', context=data['add_category'])


def add_pledged_items_list(request):
    if request.method == "POST":
        form = PledgedItemsListForm(request.POST)

        if form.is_valid():
            list = form.save(commit=False)
            list.save()
    else:
        data['add_pledged_items_list']['func'] = PledgedItemsListForm()
    return render(request, 'Lombard/add_pledged_items_list.html', context=data['add_pledged_items_list'])


def add_contract(request):
    if request.method == "POST":
        form = ContractForm(request.POST)

        if form.is_valid():
            if int(request.POST['Contract_id']) == int(Contracts.objects.all().count()+1):
                contract = form.save(commit=False)
                contract.save()
            else:
                raise ValueError(f"Указан неверный ИД")
        else:
            raise ValueError('Указана неверная дата в одном из полей')
    else:
        data['add_contract']['func'] = ContractForm()
    return render(request, 'Lombard/add_contract.html', context=data['add_contract'])


def pledged_items(request):
    return render(request, 'Lombard/pledged_items.html', context=data['pledged_items'])


def search_item(request, item):
    data['search_item']['item'] = item
    return render(request, 'Lombard/search_item.html', context=data['search_item'])


def bad_request(request, exception):
    return HttpResponseBadRequest('<h1> Мы не поняли ваш запрос <h1>')


def forbidden(request, exception):
    return HttpResponseForbidden('<h1> Доступ ЗАПРЕЩЕН <h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена. Проверьте адрес!!! </h1>')


def server_down(exception):
    return HttpResponseServerError('<h1> Сервер себя плохо чувствует. Страница недоступна <h1>')
