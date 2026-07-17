from django.urls import path
from . import views

urlpatterns = [

    path(
        "<int:booking_id>/",
        views.payment_page,
        name="payment"
    ),

    path(
        "success/<int:payment_id>/",
        views.payment_success,
        name="payment_success"
    ),

    path(
        "receipt/<int:payment_id>/",
        views.download_receipt,
        name="download_receipt"
    ),

]