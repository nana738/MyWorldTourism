# Example using Django REST Framework (DRF) for a realistic API
# You would need to install DRF: pip install djangorestframework

from rest_framework import generics
from rest_framework import serializers

# Import your models from the app
from .models import TourPackage, TourDeparture

# --- Serializers (to convert Python objects to JSON) ---

class TourDepartureSerializer(serializers.ModelSerializer):
    seats_available = serializers.ReadOnlyField() # Expose the @property from the model

    class Meta:
        model = TourDeparture
        fields = ['id', 'departure_date', 'total_seats', 'seats_booked', 'seats_available']

class TourPackageSerializer(serializers.ModelSerializer):
    # Include all related departure dates nested within the package data
    departures = TourDepartureSerializer(many=True, read_only=True)

    class Meta:
        model = TourPackage
        fields = [
            'id', 'package_name', 'slug', 'destination', 'duration_days', 
            'base_price_inr', 'itinerary_summary', 'is_active', 'departures'
        ]

# --- Views (API Endpoints) ---

class PackageListView(generics.ListAPIView):
    """API view to list all active tour packages with their departure dates."""
    queryset = TourPackage.objects.filter(is_active=True).prefetch_related('departures')
    serializer_class = TourPackageSerializer
    
# Example URL usage (in urls.py): path('api/packages/', PackageListView.as_view(), name='package-list')