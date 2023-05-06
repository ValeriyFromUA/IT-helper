from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Customer, Task, Staff, Price, Category


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
        model = Staff
        fields = ["username", "email", "password1", "password2", "city", "street", "house", "apartment", "phone"]


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["city", "street", "phone", "house", "apartment", "description"]


class FastTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["anonim_user", "phone", "city", "street", "house", "apartment", "description"]


class FullTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["phone", "city", "street", "house", "apartment", "description", "in_work", "finished", "price"]


class ConfirmationForm(forms.Form):
    confirmation_key = forms.CharField(label="confirmation key", max_length=50)


class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ['category', 'description', 'price']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'})
        }
    
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Виберіть категорію'
    )
