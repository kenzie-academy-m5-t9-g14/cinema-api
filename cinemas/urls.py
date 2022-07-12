from django.urls import path
from . import views


urlpatterns = [
    path('kinema/cinemas/', views.CinemaView.as_view()), 
    path('kinema/cinemas/<pk>/', views.CinemaDetailView.as_view()),
]