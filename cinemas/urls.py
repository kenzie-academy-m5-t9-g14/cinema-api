from django.urls import path

from . import views

urlpatterns = [
    path('cinemas/', views.CinemaView.as_view()), 
    path('cinemas/<pk>/', views.CinemaDetailView.as_view()),
]
