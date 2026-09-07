from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import BookingForm


def event_list(request):
    """Display all events on the home page."""
    events = Event.objects.all()
    return render(request, "events/event_list.html", {"events": events})


def event_detail(request, event_id):
    """Display event details and handle booking form submission."""
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.event = event
            booking.save()
            return redirect("booking_success", booking_id=booking.id)
    else:
        form = BookingForm()

    return render(request, "events/event_detail.html", {"event": event, "form": form})


def booking_success(request, booking_id):
    """Display booking confirmation."""
    from .models import Booking

    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, "events/booking_success.html", {"booking": booking})
