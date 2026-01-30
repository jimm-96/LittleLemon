from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        # Añadir instancias de prueba del modelo Menu
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=150, inventory=50)
        Menu.objects.create(title="Burger", price=120, inventory=75)

    def test_getall(self):
        # Recuperar todos los objetos Menu
        response = self.client.get('/restaurant/menu/')
        
        # Obtener todos los menús de la base de datos
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        # Comparar la respuesta con los datos serializados
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serializer.data)
