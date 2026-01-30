# Little Lemon Restaurant API

A Django REST Framework backend for the Little Lemon restaurant, featuring Menu and Table Booking APIs with user authentication.

## Features

- MySQL database connection
- Menu API (CRUD operations)
- Table Booking API with authentication
- User registration and token authentication (Djoser)
- Unit tests for models and views

## API Endpoints

### Menu API
- `GET /restaurant/menu/` - List all menu items
- `POST /restaurant/menu/` - Create a new menu item
- `GET /restaurant/menu/<id>` - Get a specific menu item
- `PUT /restaurant/menu/<id>` - Update a menu item
- `DELETE /restaurant/menu/<id>` - Delete a menu item

### Booking API (Authentication Required)
- `GET /restaurant/booking/tables/` - List all bookings
- `POST /restaurant/booking/tables/` - Create a new booking
- `GET /restaurant/booking/tables/<id>/` - Get a specific booking
- `PUT /restaurant/booking/tables/<id>/` - Update a booking
- `DELETE /restaurant/booking/tables/<id>/` - Delete a booking

### Authentication
- `POST /auth/users/` - Register a new user
- `POST /auth/token/login/` - Login and get token
- `POST /auth/token/logout/` - Logout

## Setup

1. Create a virtual environment and activate it
2. Install dependencies: `pip install django djangorestframework djoser mysqlclient`
3. Configure MySQL database in `settings.py`
4. Run migrations: `python manage.py migrate`
5. Start server: `python manage.py runserver`

## Testing

Run unit tests with:
```
python manage.py test
```

## Testing with Insomnia

1. Register a user: POST to `/auth/users/` with `username`, `password`, `email`
2. Get token: POST to `/auth/token/login/` with `username`, `password`
3. Use the token in Authorization header: `Token <your-token>`
4. Make requests to booking endpoints