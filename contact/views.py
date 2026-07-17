from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def contact(request):

    if request.method == "POST":

        Contact.objects.create(

            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message")

        )

        messages.success(request, "Message Sent Successfully!")

        return redirect("home")

    return redirect("home")

# Create your views here.
