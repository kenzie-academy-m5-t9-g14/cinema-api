from django.urls import path
from .views import SeatView,SeatDetailView, SeatSessionView

urlpatterns = [
    path("movie_theater/<pk>/seats/",SeatView.as_view()),
    path("seats/<int:pk>/",SeatDetailView.as_view()),
    path("movie_sessions/<str:movie_session_id>/seats/",SeatSessionView.as_view())
]