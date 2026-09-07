from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    venue = models.CharField(max_length=200)
    capacity = models.IntegerField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    tickets = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.event.title}"
