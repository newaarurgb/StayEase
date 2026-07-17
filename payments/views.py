from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from bookings.models import Booking
from .models import Payment
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor


def payment_page(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    if request.method == "POST":

        payment = Payment.objects.create(
            booking=booking,
            user=request.user,
            amount=booking.hotel.price,
            payment_method=request.POST.get("payment_method"),
            status="Success"
        )

        return redirect("payment_success", payment_id=payment.id)

    return render(
        request,
        "payments/payment.html",
        {
            "booking": booking
        }
    )


def payment_success(request, payment_id):

    payment = get_object_or_404(
        Payment,
        id=payment_id,
        user=request.user
    )

    return render(
        request,
        "payments/payment_success.html",
        {
            "payment": payment
        }
    )


def download_receipt(request, payment_id):

    payment = get_object_or_404(
        Payment,
        id=payment_id,
        user=request.user
    )

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = (
        f'attachment; filename="Receipt_{payment.id}.pdf"'
    )

    p = canvas.Canvas(response)

    p.setTitle("StayEase Receipt")

    # Heading
    p.setFont("Helvetica-Bold", 24)
    p.setFillColor(HexColor("#ffb400"))
    p.drawString(170, 800, "StayEase")

    p.setFont("Helvetica-Bold", 18)
    p.setFillColor(HexColor("#000000"))
    p.drawString(170, 775, "Payment Receipt")

    y = 720

    p.setFont("Helvetica", 13)

    p.drawString(70, y, f"Receipt ID : {payment.id}")
    y -= 30

    p.drawString(70, y, f"Customer : {payment.user.username}")
    y -= 30

    p.drawString(70, y, f"Hotel : {payment.booking.hotel.name}")
    y -= 30

    p.drawString(70, y, f"Amount : ₹{payment.amount}")
    y -= 30

    p.drawString(70, y, f"Payment Status : {payment.status}")
    y -= 30

    p.drawString(70, y, f"Payment Date : {payment.payment_date}")
    y -= 50

    p.setFont("Helvetica-Bold", 14)

    p.drawString(
        70,
        y,
        "Thank you for booking with StayEase!"
    )

    p.showPage()
    p.save()

    return response


# Create your views here.