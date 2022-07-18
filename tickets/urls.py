from django.urls import path
from . import views

urlpatterns = [
    path("tickets/", views.TicketView.as_view()),
    path("tickets/<pk>/", views.TicketDetailView.as_view()),
]