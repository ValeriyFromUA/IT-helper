from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Task, Category


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserDataForm(ModelForm):
    class Meta:
        model = User
        fields = ['city', 'street', 'house', 'apartment', 'phone']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class TaskForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Task
        fields = ['description', 'category']


class ConfirmationForm(forms.Form):
    confirmation_key = forms.CharField(label="confirmation key", max_length=50)
