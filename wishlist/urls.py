from django.urls import path
from . import views

urlpatterns = [
    path("add/<int:hotel_id>/", views.add_to_wishlist, name="add_to_wishlist"),
    path("", views.my_wishlist, name="my_wishlist"),
]