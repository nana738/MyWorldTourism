from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TourPackage


class PackageListView(APIView):
    def get(self, request):
        packages = TourPackage.objects.filter(is_active=True)

        data = []
        for package in packages:
            data.append({
                "id": package.id,
                "name": package.name,
                "destination": package.destination,
                "price": package.price,
                "description": package.description,
            })

        return Response(data)
