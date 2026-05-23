from django.contrib import admin
from .models import EventRegistration


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'age', 'registered_at']
    list_filter = ['registered_at']
    search_fields = ['full_name', 'email']
