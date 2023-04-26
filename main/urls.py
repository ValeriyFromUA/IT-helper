from django.urls import path

from .views import (
    AboutView,
    ConfirmView,
    DeleteTaskView,
    EditProfileView,
    FastTaskView,
    HomeView,
    LoginView,
    LogoutView,
    NewTaskView,
    RegistrationView,
    StaffMainView,
    StaffTaskView,
    TaskView,
    UserProfileView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("confirm/", ConfirmView.as_view(), name="confirm"),
    path("task/<str:pk>/delete/", DeleteTaskView.as_view(), name="delete_task"),
    path("edit_profile/<str:pk>", EditProfileView.as_view(), name="edith_profile"),
    path("home/", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("new_task/", NewTaskView.as_view(), name="new_task"),
    path("fast_task/", FastTaskView.as_view(), name="fast_task"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("staff/main/", StaffMainView.as_view(), name="staff_main"),
    path("task/<str:pk>/", TaskView.as_view(), name="task"),
    path("profile/<str:pk>/", UserProfileView.as_view(), name="profile"),
    path("staff/registration/", RegistrationView.as_view(), name="staff_registration"),
    path("staff/login/", RegistrationView.as_view(), name="staff_login"),
    path("staff/task/<str:pk>/", StaffTaskView.as_view(), name="staff_task"),
]
