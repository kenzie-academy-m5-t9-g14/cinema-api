from django.urls import path
from .views import SeatView,SeatDetailView

urlpatterns = [
    path("movie_theater/<pk>/seats/",SeatView.as_view()),
    path("seats/<int:pk>/",SeatDetailView.as_view())
]