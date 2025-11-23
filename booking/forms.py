from django import forms
from .models import Appointment
from django.core.exceptions import ValidationError
from datetime import datetime, date

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['service', 'date', 'time', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows':3}),
        }

    def clean(self):
        cleaned = super().clean()
        service = cleaned.get('service')
        appt_date = cleaned.get('date')
        appt_time = cleaned.get('time')

        if appt_date and appt_date < date.today():
            raise ValidationError("You cannot book an appointment in the past.")

        if service and appt_date and appt_time:
            conflicts = Appointment.objects.filter(
                service=service,
                date=appt_date,
                time=appt_time,
                status__in=['pending','confirmed']
            )
            if conflicts.exists():
                raise ValidationError("Selected time is already booked for this service. Please choose another time.")
