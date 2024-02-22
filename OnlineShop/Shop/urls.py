from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FigureViewSet, CartViewSet, CartProductViewSet, CustomerViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'figures', FigureViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-products', CartProductViewSet)
router.register(r'customers', CustomerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)