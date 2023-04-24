from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Category, Customer, Task


class NewUserForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ["username", "email", "password1", "password2"]


class UserDataForm(ModelForm):
    class Meta:
        model = Customer
        fields = ["city", "street", "house", "apartment", "phone"]


class NewStaffForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ["username", "email", "password1", "password2"]


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]


class TaskForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Task
        fields = ["city", "street", "house", "apartment", "description", "category"]


class ConfirmationForm(forms.Form):
    confirmation_key = forms.CharField(label="confirmation key", max_length=50)
