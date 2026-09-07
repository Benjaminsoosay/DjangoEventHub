from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["customer_name", "email", "phone", "tickets"]
        widgets = {
            "customer_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "tickets": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
        }
