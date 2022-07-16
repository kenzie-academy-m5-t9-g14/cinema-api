from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("login/", views.LoginUserView.as_view()),
    path("users/<str:pk>/", views.UserDetailView.as_view())
]