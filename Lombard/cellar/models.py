from django.contrib import admin
from django.contrib.auth import authenticate
from django.db import models
from django.contrib.auth.models import AbstractUser


class Posts(models.Model):
    Post_id = models.PositiveIntegerField(primary_key=True)
    content = models.CharField(max_length=30)
    Salary = models.IntegerField(default=14375)

    class Meta:
        verbose_name_plural = "Должности"

    def __str__(self):
        return f"{self.content}"


class Divisions(models.Model):
    Division_id = models.PositiveIntegerField(primary_key=True)
    Division_name = models.CharField(max_length=30)
    Street_address = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Отделения"

    def __str__(self):
        return f"{self.Division_name}"


class Clients(models.Model):
    Client_id = models.PositiveIntegerField(primary_key=True)
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Phone_number = models.BigIntegerField()
    Passport_series = models.IntegerField()
    Passport_number = models.IntegerField()

    class Meta:
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.Last_name} {self.First_name} ({self.Client_id})"


class Employees(models.Model):
    Employee_id = models.PositiveIntegerField(primary_key=True)
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    Phone_number = models.BigIntegerField()
    Division_id = models.ForeignKey(Divisions, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.Last_name} {self.First_name} ({self.Post_id})"

class Categories(models.Model):
    Category_id = models.PositiveIntegerField(primary_key=True)
    Division_id = models.ForeignKey(Divisions, on_delete=models.CASCADE)
    Refund_possibility = models.BooleanField()

    class Meta:
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.Category_id} степень"

class Pledged_items_list(models.Model):
    Pledged_items_list_id = models.PositiveIntegerField(primary_key=True)
    Pledged_item_name = models.CharField(max_length=30)
    Price = models.IntegerField()
    Quality = models.IntegerField()
    Category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Заложенная вещь"

    def __str__(self):
        return f"{self.Pledged_item_name} ({self.Price} руб.)"

class Contracts(models.Model):
    Contract_id = models.PositiveIntegerField(primary_key=True)
    Sign_date = models.DateTimeField()
    Expiration_date = models.DateTimeField()
    Employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    Bail = models.IntegerField()
    Pledged_items_list_id = models.ForeignKey(Pledged_items_list, on_delete=models.CASCADE)
    Commision_fee = models.IntegerField()
    Client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Контракты"

    def __str__(self):
        return f"№{self.Contract_id} - {self.Bail} руб."