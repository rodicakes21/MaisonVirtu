from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, Appointment
from .forms import AppointmentForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def index(request):
    services = Service.objects.all()
    return render(request, 'index.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    form = AppointmentForm(initial={'service': service})
    return render(request, 'service_detail.html', {'service': service, 'form': form})

@login_required
def book_service(request, pk=None):
    """
    If pk provided we preselect service, else user chooses service on form.
    """
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appt = form.save(commit=False)
            appt.user = request.user
            appt.save()
            return redirect('my_appointments')
    else:
        if pk:
            service = get_object_or_404(Service, pk=pk)
            form = AppointmentForm(initial={'service': service})
        else:
            form = AppointmentForm()
    return render(request, 'book.html', {'form': form})

@login_required
def my_appointments(request):
    appts = request.user.appointments.order_by('-date', '-time')
    return render(request, 'my_appointments.html', {'appointments': appts})

@login_required
def cancel_appointment(request, pk):
    appt = get_object_or_404(Appointment, pk=pk, user=request.user)
    appt.status = 'cancelled'
    appt.save()
    return redirect('my_appointments')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
