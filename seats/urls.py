from django.urls import path
from . import views

urlpatterns = [
    path("movie_theater/<pk>/seats/",views.SeatView.as_view()),
    path("seats/<str:pk>/",views.SeatDetailView.as_view()),
    path("seats/",views.SeatListView.as_view())
]