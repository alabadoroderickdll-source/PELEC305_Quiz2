from django.db import models


class EventRegistration(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField()
    password = models.CharField(max_length=255)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.email})"

    class Meta:
        ordering = ['-registered_at']
        verbose_name = 'Event Registration'
        verbose_name_plural = 'Event Registrations'
