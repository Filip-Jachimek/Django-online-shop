from django.contrib import admin
from django.urls import path, include  # Dodaj include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Shop.urls')),  # Dołącz adresy URL z aplikacji Shop
]

