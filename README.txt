================================================================================
                    LITTLE LEMON RESTAURANT API
================================================================================

Proyecto Django REST Framework para gestionar reservas de mesas y menú del 
restaurante Little Lemon.

================================================================================
                         RUTAS API DISPONIBLES
================================================================================

MENU API
--------
GET    /restaurant/menu/              - Listar todos los items del menú
POST   /restaurant/menu/              - Crear nuevo item del menú
GET    /restaurant/menu/<id>          - Obtener item específico
PUT    /restaurant/menu/<id>          - Actualizar item del menú
DELETE /restaurant/menu/<id>          - Eliminar item del menú

BOOKING API (Reservas de mesas - Requiere autenticación)
---------------------------------------------------------
GET    /restaurant/booking/tables/       - Listar todas las reservas
POST   /restaurant/booking/tables/       - Crear nueva reserva
GET    /restaurant/booking/tables/<id>/  - Obtener reserva específica
PUT    /restaurant/booking/tables/<id>/  - Actualizar reserva
DELETE /restaurant/booking/tables/<id>/  - Eliminar reserva

AUTENTICACIÓN (Djoser)
----------------------
POST   /auth/users/                   - Registrar nuevo usuario
POST   /auth/token/login/             - Iniciar sesión (obtener token)
POST   /auth/token/logout/            - Cerrar sesión
POST   /restaurant/api-token-auth/    - Obtener token de autenticación

================================================================================
                      INSTRUCCIONES DE PRUEBA
================================================================================

1. CONFIGURAR BASE DE DATOS MYSQL
   - Crear base de datos llamada "LittleLemon"
   - Configurar credenciales en settings.py

2. INSTALAR DEPENDENCIAS
   pip install -r requirements.txt

3. EJECUTAR MIGRACIONES
   python manage.py migrate

4. INICIAR SERVIDOR
   python manage.py runserver

5. PROBAR CON INSOMNIA/POSTMAN
   
   a) Registrar usuario:
      POST http://127.0.0.1:8000/auth/users/
      Body: {"username": "testuser", "password": "testpass123", "email": "test@test.com"}
   
   b) Obtener token:
      POST http://127.0.0.1:8000/auth/token/login/
      Body: {"username": "testuser", "password": "testpass123"}
   
   c) Crear reserva (con token):
      POST http://127.0.0.1:8000/restaurant/booking/tables/
      Headers: Authorization: Token <tu-token>
      Body: {"name": "John Doe", "no_of_guests": 4, "booking_date": "2026-02-15T19:00:00Z"}

6. EJECUTAR PRUEBAS UNITARIAS
   python manage.py test

================================================================================
                         TECNOLOGÍAS UTILIZADAS
================================================================================

- Python 3.9
- Django 4.2
- Django REST Framework
- MySQL
- Djoser (autenticación)
- Token Authentication

================================================================================
