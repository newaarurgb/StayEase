from django.urls import path
from . import views

urlpatterns = [
    path("<int:hotel_id>/", views.book_hotel, name="book_hotel"),
    path("success/", views.booking_success, name="booking_success"),
    path('book/<int:hotel_id>/', views.book_hotel, name='book_hotel'),
]