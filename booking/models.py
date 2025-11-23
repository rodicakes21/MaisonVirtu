from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField(default=60)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

APPOINTMENT_STATUS = [
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('cancelled', 'Cancelled'),
    ('completed', 'Completed'),
]

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=APPOINTMENT_STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-time']

    def __str__(self):
        return f"{self.user.username} - {self.service.name} on {self.date} at {self.time}"
