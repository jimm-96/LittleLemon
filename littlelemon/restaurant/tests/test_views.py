from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of Menu model
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=150, inventory=50)
        Menu.objects.create(title="Burger", price=120, inventory=75)

    def test_getall(self):
        # Retrieve all Menu objects
        response = self.client.get('/restaurant/menu/')
        
        # Get all menus from the database
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        # Compare response with serialized data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serializer.data)
