from django.urls import path
from . import views

urlpatterns = [
    path("kinema/users/", views.UserView.as_view()),
    path("kinema/login/", views.LoginUserView.as_view()),
]