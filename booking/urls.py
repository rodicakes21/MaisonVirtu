from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service/<int:pk>/', views.service_detail, name='service_detail'),
    path('book/', views.book_service, name='book'),
    path('book/<int:pk>/', views.book_service, name='book_service'),
    path('my-appointments/', views.my_appointments, name='my_appointments'),
    path('cancel/<int:pk>/', views.cancel_appointment, name='cancel_appointment'),
    path('signup/', views.signup_view, name='signup'),
]
