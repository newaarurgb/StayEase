from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from hotels.models import Hotel
from .models import Booking
from .forms import BookingForm


def book_hotel(request, hotel_id):

    print("Request Method:", request.method)

    hotel = get_object_or_404(Hotel, id=hotel_id)

    if request.method == "POST":

        print("POST received")

        form = BookingForm(request.POST)

        if form.is_valid():

            print("Form is VALID")

            booking = form.save(commit=False)
            booking.hotel = hotel

            if request.user.is_authenticated:
                booking.user = request.user

            booking.save()

            print("Booking Saved:", booking.id)

            hotel.available_rooms -= 1
            hotel.save()

            return redirect("payment", booking_id=booking.id)

        else:

            print("FORM ERRORS")
            print(form.errors)

    else:

        form = BookingForm()

    return render(request, "booking_form.html", {
        "hotel": hotel,
        "form": form
    })

def booking_success(request):
    return render(request, "booking_success.html")
# Create your views here.
