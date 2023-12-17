from django import forms
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ("Post_id", "content", "Salary")

class DivisionForm(forms.ModelForm):

    class Meta:
        model = Divisions
        fields = ("Division_id", "Division_name", "Street_address")


class ClientForm(forms.ModelForm):

    class Meta:
        model = Clients
        fields = ("Client_id", "First_name", "Last_name", "Phone_number",
                    "Passport_series", "Passport_number")


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employees
        fields = ("Employee_id", "First_name", "Last_name",
                    "Post_id", "Phone_number", "Division_id")


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Categories
        fields = ("Category_id", "Division_id", "Refund_possibility")


class PledgedItemsListForm(forms.ModelForm):

    class Meta:
        model = Pledged_items_list
        fields = ("Pledged_items_list_id", "Pledged_item_name", "Price",
                    "Quality", "Category_id")


class ContractForm(forms.ModelForm):

    class Meta:
        model = Contracts
        fields = ("Contract_id", "Sign_date", "Expiration_date", "Employee_id",
                    "Bail", "Pledged_items_list_id", "Commision_fee", "Client_id")
