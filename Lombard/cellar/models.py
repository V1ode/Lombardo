from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    Post_id = models.PositiveIntegerField(primary_key=True)
    content = models.CharField(max_length=30)
    Salary = models.IntegerField(default=14375)

class Divisions(models.Model):
    Division_id = models.PositiveIntegerField(primary_key=True)
    Division_name = models.CharField(max_length=30)
    Street_address = models.CharField(max_length=30)

class Clients(models.Model):
    Client_id = models.PositiveIntegerField(primary_key=True)
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Phone_number = models.BigIntegerField()
    Passport_series = models.IntegerField()
    Passport_number = models.IntegerField()

class Employees(models.Model):
    Employee_id = models.PositiveIntegerField(primary_key=True)
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    Phone_number = models.BigIntegerField()
    Division_id = models.ForeignKey(Divisions, on_delete=models.CASCADE)

class Categories(models.Model):
    Category_id = models.PositiveIntegerField(primary_key=True)
    Division_id = models.ForeignKey(Divisions, on_delete=models.CASCADE)
    Refund_possibility = models.BooleanField()

class Pledged_items_list(models.Model):
    Pledged_items_list_id = models.PositiveIntegerField(primary_key=True)
    Pledged_item_name = models.CharField(max_length=30)
    Price = models.IntegerField()
    Quality = models.IntegerField()
    Category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)

class Contracts(models.Model):
    Contract_id = models.PositiveIntegerField(primary_key=True)
    Sign_date = models.DateTimeField()
    Expiration_date = models.DateTimeField()
    Employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    Bail = models.IntegerField()
    Pledged_items_list_id = models.ForeignKey(Pledged_items_list, on_delete=models.CASCADE)
    Commision_fee = models.IntegerField()
    Client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
