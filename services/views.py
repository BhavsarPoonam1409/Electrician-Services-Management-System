from django.shortcuts import render
from .models import Service
from .models import Booking

# Create your views here.
# def services(request):
#     return render(request,"services/services.html")

def services(request):
    services = Service.objects.all()

    context = {
        "services" : services
    }
    return render(request, "services/services.html",context)


def book_service(request, service_id):

    service = Service.objects.get(id=service_id)

    if(request.method == "POST"):

        # Booking.objects.create(
        #     customer_name=request.POST['customer_name'],
        #     mobile=request.POST['mobile'],
        #     service=request.POST['service.name'],
        #     price=service.price,
        #     location=request.POST['location'],
        #     address=request.POST['address'],
        #     date=request.POST['date'],
        #     time=request.POST['time']
        # )
        #direct create function me data get krne ke liye model ka
        Booking.objects.create(
            customer_name=request.POST.get('customer_name'),
            mobile=request.POST.get('mobile'),
            service=service.name,
            price=service.price,
            location=request.POST.get('location'),
            address=request.POST.get('address'),
            date=request.POST.get('date'),
            time=request.POST.get('time')
        )
        context = {
            "service": service
        }

        return render(request,"services/booking_success.html",context)

    context = {
        "service": service
    }

    return render(request,"services/book_services.html",context)

def update_booking(request, booking_id):

    booking = Booking.objects.get(id=booking_id)

    if(request.method == "POST"):

        booking.customer_name = request.POST.get('customer_name')
        booking.mobile = request.POST.get('mobile')
        booking.location = request.POST.get('location')
        booking.address = request.POST.get('address')
        booking.date = request.POST.get('date')
        booking.time = request.POST.get('time')

        booking.save()

        context = {
            "booking" : booking
        }
        return render(request,"services/booking_success.html",context)

    context = {
        "booking": booking
    }

    return render(request,"services/update_booking.html",context)

def cancel_booking(request, booking_id):

    booking = Booking.objects.get(id=booking_id)
    booking.delete()
    return render(request,"services/cancel_success.html")