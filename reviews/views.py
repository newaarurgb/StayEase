from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from hotels.models import Hotel
from .models import Review
from .forms import ReviewForm


@login_required
def add_review(request, hotel_id):

    hotel = get_object_or_404(Hotel,id=hotel_id)

    if request.method=="POST":

        form=ReviewForm(request.POST)

        if form.is_valid():

            review=form.save(commit=False)

            review.hotel=hotel

            review.user=request.user

            review.save()

            return redirect('hotel_details',id=hotel.id)

    else:

        form=ReviewForm()

    return render(request,'add_review.html',{
        'form':form,
        'hotel':hotel
    })

# Create your views here.
