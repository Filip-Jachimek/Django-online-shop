from django.test import TestCase
from django.http import HttpRequest
from ..models import Figure



class FigureModelTestCase(TestCase):
    def setUp(self):
        self.figure = Figure.objects.create(
            name="Test Figure",
            description="Test description",
            price_usd=10.99,
            availability=True,
            race="human",
            faction="empire",
            height_cm=15.5
        )
    
    def test_figure_creation(self):
        figure = Figure.objects.get(name="Test Figure")
        self.assertEqual(figure.name, "Test Figure")
        self.assertEqual(figure.description, "Test description")
        self.assertAlmostEqual(float(figure.price_usd), 10.99)
        self.assertTrue(figure.availability)
        self.assertEqual(figure.race, "human")
        self.assertEqual(figure.faction, "empire")
        self.assertEqual(figure.height_cm, 15.5)

    def test_figure_update(self):
        self.figure.price_usd = 12.99
        self.figure.save()
        updated_figure = Figure.objects.get(name="Test Figure")
        self.assertAlmostEqual(float(updated_figure.price_usd), 12.99)

    def test_figure_deletion(self):
        self.figure.delete()
        self.assertEqual(Figure.objects.filter(name="Test Figure").count(), 0)
