from django.urls import path
from . import views

urlpatterns = [
    path("movie_session/<str:movie_session_id>/ticket/", views.TicketView.as_view()),
    path("tickets/<pk>/", views.TicketDetailView.as_view()),
    path("tickets/", views.TicketListView.as_view()),
]