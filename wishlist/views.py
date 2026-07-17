from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from hotels.models import Hotel
from .models import Wishlist


@login_required
def add_to_wishlist(request, hotel_id):

    hotel = get_object_or_404(Hotel, id=hotel_id)

    wishlist, created = Wishlist.objects.get_or_create(
        user=request.user,
        hotel=hotel
    )

    if created:
        messages.success(request, "❤️ Hotel added to your wishlist!")
    else:
        messages.info(request, "This hotel is already in your wishlist.")

    return redirect("my_wishlist")


@login_required
def my_wishlist(request):

    wishlist = Wishlist.objects.filter(user=request.user)

    return render(
        request,
        "wishlist.html",
        {
            "wishlist": wishlist
        }
    )