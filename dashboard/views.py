from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from bookings.models import Booking
from wishlist.models import Wishlist
from payments.models import Payment
from reviews.models import Review


@login_required
def dashboard(request):

    bookings = Booking.objects.filter(user=request.user)
    wishlist = Wishlist.objects.filter(user=request.user)
    payments = Payment.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)

    context = {
        "bookings": bookings,
        "wishlist": wishlist,
        "payments": payments,
        "reviews": reviews,

        "booking_count": bookings.count(),
        "wishlist_count": wishlist.count(),
        "payment_count": payments.count(),
        "review_count": reviews.count(),
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )