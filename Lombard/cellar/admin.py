from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from .models import *

# admin.site.register(Posts)
# admin.site.register(Divisions)
# admin.site.register(Clients)
# admin.site.register(Employees)
# admin.site.register(Categories)
# admin.site.register(Pledged_items_list)
# admin.site.register(Contracts)

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ("Post_id", "content", "Salary")


@admin.register(Divisions)
class DivisionsAdmin(admin.ModelAdmin):
    list_display = ("Division_id", "Division_name", "Street_address")


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ("Client_id", "First_name", "Last_name", "Phone_number",
                    "Passport_series", "Passport_number")


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ("Employee_id", "First_name", "Last_name",
                    "Post_id", "Phone_number", "Division_id")


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("Category_id", "Division_id", "Refund_possibility")


@admin.register(Pledged_items_list)
class Pledged_items_listAdmin(admin.ModelAdmin):
    list_display = ("Pledged_items_list_id", "Pledged_item_name", "Price",
                    "Quality", "Category_id")


@admin.register(Contracts)
class ContractsAdmin(admin.ModelAdmin):
    list_display = ("Contract_id", "Sign_date", "Expiration_date", "Employee_id",
                    "Bail", "Pledged_items_list_id", "Commision_fee", "Client_id")