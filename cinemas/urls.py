from django.urls import path
from . import views


urlpatterns = [
    path('kinema/cinemas/', views.ListCreateCinemaView.as_view()),  # post/get
    path('kinema/cinemas/<pk>/', views.RetrieveUpdateDestroyCinemaView.as_view())  # delete/patch/get_one
]