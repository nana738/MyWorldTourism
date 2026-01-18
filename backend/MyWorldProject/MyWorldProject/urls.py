from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from tours.views import PackageListView


def home(request):
    return JsonResponse({
        "status": "MyWorldTourism backend is running",
        "endpoints": {
            "packages": "/api/packages/"
        }
    })


urlpatterns = [
    path("", home, name="home"),  # 👈 root URL
    path("admin/", admin.site.urls),
    path("api/packages/", PackageListView.as_view(), name="package-list"),
]
