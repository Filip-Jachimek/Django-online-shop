from rest_framework import serializers
from .models import Figure
from .order import Order, OrderProduct
from .customer import Customer
from .cart import Cart, CartProduct

class FigureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Figure
        fields = ['id', 'name', 'description', 'price_usd', 'availability', 'race', 'faction', 'height_cm', 'image']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'products', 'order_date', 'status', 'total_price']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'shipping_address']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'customer', 'products', 'added_date']

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ['id', 'cart', 'figure', 'quantity' ]
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'shipping_address']