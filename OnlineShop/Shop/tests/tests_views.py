from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Figure 
from ..cart import Cart, CartProduct
from ..customer import Customer

import pdb

class FigureViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.figure_data = {
            'name': 'Test Figure',
            'description': 'Test description',
            'price_usd': 10.99,
            'availability': True,
            'race': 'human',
            'faction': 'empire',
            'height_cm': 15.5
        }
        self.figure = Figure.objects.create(**self.figure_data)

    def test_figure_list_view(self):
        response = self.client.get(reverse('figure-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming only one figure is created in setUp

    def test_figure_detail_view(self):
        response = self.client.get(reverse('figure-detail', kwargs={'pk': self.figure.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.figure_data['name'])

    def test_figure_creation_view(self):
        response = self.client.post(reverse('figure-list'), self.figure_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_figure_update_view(self):
        updated_price = 12.99
        updated_data = self.figure_data.copy()
        updated_data['price_usd'] = updated_price
        response = self.client.put(reverse('figure-detail', kwargs={'pk': self.figure.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertAlmostEqual(float(Figure.objects.get(pk=self.figure.pk).price_usd), updated_price)

    def test_figure_deletion_view(self):
        response = self.client.delete(reverse('figure-detail', kwargs={'pk': self.figure.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CartViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.figure = Figure.objects.create(name="Test Figure", price_usd=10.99)
        self.user = User.objects.create(username="testuser")
        self.customer = Customer.objects.create(user=self.user)
        self.cart_data = {
            'customer': self.customer.id,  # Użyj identyfikatora klienta
            'products': [{'figure': self.figure.pk, 'quantity': 1}]
        }
        self.cart = Cart.objects.create(customer=self.customer) 

    def test_create_cart_view(self):
        initial_cart_count = Cart.objects.count()  # Pobierz początkową liczbę koszyków

        response = self.client.post(reverse('cart-list'), self.cart_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Sprawdź, czy liczba koszyków zwiększyła się o 1
        self.assertEqual(Cart.objects.count(), initial_cart_count + 1)
