from django.contrib import admin
from django.urls import path, include

api_urls = [
    path("", include("advert.urls")),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include((api_urls, ""))),
]
