from django.contrib import admin
from .models import Service, Appointment

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_minutes', 'price')
    search_fields = ('name',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('service', 'user', 'date', 'time', 'status', 'created_at')
    list_filter = ('status', 'service', 'date')
    search_fields = ('user__username', 'user__email', 'service__name')
    actions = ['mark_confirmed', 'mark_cancelled']

    def mark_confirmed(self, request, queryset):
        queryset.update(status='confirmed')
    mark_confirmed.short_description = "Mark selected appointments as confirmed"

    def mark_cancelled(self, request, queryset):
        queryset.update(status='cancelled')
    mark_cancelled.short_description = "Mark selected appointments as cancelled"
