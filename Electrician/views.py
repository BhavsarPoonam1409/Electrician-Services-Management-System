from django.shortcuts import render
from services.models import Booking


def home(request):

    bookings = Booking.objects.all()

    return render(request,"home.html",{"bookings": bookings})

# def home(reuqest):
#     return render(reuqest,'home.html')

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    return render(request,"contact.html")