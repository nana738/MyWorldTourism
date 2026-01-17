# Assuming a standard Django project setup

from django.db import models

class TourPackage(models.Model):
    """Defines the structure for a single tour package."""

    package_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, help_text="URL-friendly identifier")
    destination = models.CharField(max_length=100)
    duration_days = models.PositiveSmallIntegerField()
    base_price_inr = models.DecimalField(max_digits=10, decimal_places=2)
    inclusions = models.TextField()
    itinerary_summary = models.TextField()
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.package_name} to {self.destination}"

class TourDeparture(models.Model):
    """Defines specific dates and available seats for a package."""
    
    package = models.ForeignKey(
        TourPackage,
        on_delete=models.CASCADE,
        related_name='departures'
    )
    departure_date = models.DateField()
    total_seats = models.PositiveSmallIntegerField(default=40)
    seats_booked = models.PositiveSmallIntegerField(default=0)
    
    class Meta:
        unique_together = ('package', 'departure_date')

    @property
    def seats_available(self):
        """Calculates available seats."""
        return self.total_seats - self.seats_booked

    def __str__(self):
        return f"{self.package.package_name} on {self.departure_date} ({self.seats_available} seats left)"