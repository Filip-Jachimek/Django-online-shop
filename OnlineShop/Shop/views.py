from rest_framework import viewsets
from rest_framework.response import Response
from .models import Figure
from .cart import Cart, CartProduct
from .customer import Customer
from .serializers import FigureSerializer, CartSerializer, CartProductSerializer, CustomerSerializer
from django.http import HttpResponse


class FigureViewSet(viewsets.ModelViewSet):
    queryset = Figure.objects.all()
    serializer_class = FigureSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Figure.objects.all()
    serializer_class = FigureSerializer

import logging

logger = logging.getLogger(__name__)

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def add_to_cart(self, request, pk=None):
        figure_id = request.data.get('figure_id')
        logger.debug(f"Received request to add figure with ID {figure_id} to cart.")
        quantity = request.data.get('quantuty', 1)

        if not figure_id:
            return Response({'error': 'Figure ID is required'}, status=400)
        
        try:
            figure = Figure.objects.get(pk=figure_id)
        except Figure.DoesNotExist:
            return Response({'error': 'Figure not found'}, status=404)
        
        cart, _ = Cart.objects.get_or_create(customer=request.user.customer)
        cart_product, created = CartProduct.objects.get_or_create(cart=cart, figure=figure)
        if not created:
            cart_product.quantity += int(quantity)
            cart_product.save()
            
        return Response({'success': 'Product added to cart'})
    
    def remove_from_cart(self, request, pk=None):
        cart_product_id = request.data.get('cart_product_id')
        logger.debug(f"Received request to remove cart product with ID {cart_product_id} from cart.")

        
        if not cart_product_id:
            return Response({'error': 'Cart product ID is required'}, status=400)
        
        try:
            cart_product = CartProduct.objects.get(pk=cart_product_id)
        except CartProduct.DoesNotExist:
            return Response({'error': 'Cart product not found'}, status=404)
        
        cart_product.delete()
        return Response({'success': 'Product removed from cart'})

    def update_cart_product(self, request, pk=None):
        cart_product_id = request.data.get('cart_product_id')
        logger.debug(f"Received request to update cart product with ID {cart_product_id}.")
        quantity = request.data.get('quantity', 1)
        
        if not cart_product_id:
            return Response({'error': 'Cart product ID is required'}, status=400)
        
        try:
            cart_product = CartProduct.objects.get(pk=cart_product_id)
        except CartProduct.DoesNotExist:
            return Response({'error': 'Cart product not found'}, status=404)
        
        cart_product.quantity = int(quantity)
        cart_product.save()
        return Response({'success': 'Cart product updated'})
    
class CartProductViewSet(viewsets.ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer