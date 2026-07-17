from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Hotel
from reviews.models import Review
from django.contrib.auth.decorators import login_required


def home(request):

    hotels = Hotel.objects.filter(available=True)

    city = request.GET.get('city')
    hotel_type = request.GET.get('hotel_type')
    rating = request.GET.get('rating')
    price = request.GET.get('price')

    if city:
        hotels = hotels.filter(city__icontains=city)

    if hotel_type:
        hotels = hotels.filter(hotel_type=hotel_type)

    if rating:
        hotels = hotels.filter(rating__gte=rating)

    if price:
        hotels = hotels.filter(price__lte=price)

    return render(request, "home.html", {
        "hotels": hotels
    })

@login_required
def hotel_details(request, hotel_id):

    hotel = get_object_or_404(Hotel, id=hotel_id)

    if request.method == "POST":

        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        Review.objects.create(
            hotel=hotel,
            user=request.user,
            rating=rating,
            comment=comment
        )

        messages.success(request, "Review Submitted Successfully!")
        return redirect("hotel_details", hotel_id=hotel.id)

    return render(request, "hotel_details.html", {"hotel": hotel})