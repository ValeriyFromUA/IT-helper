from django.urls import path
from views import (AboutView, ConfirmView, DeleteTaskView, EditProfileView, HomeView, LogoutView, LoginView,
                   NewTaskView, StaffMainView, TaskView, UserProfileView, RegistrationView)

urlpatterns = [
    path('', views.home, name="home"),

]
