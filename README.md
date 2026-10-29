# Library Management API

## Project Description
A Django REST API for managing a library's books, authors, and categories.

## Features
- User registration and login.
- JWT authentication.
- View user profile.
- List, create, update, and delete books.
- Manage authors and categories.

## Technologies
- Python
- Django
- Django REST Framework
- Simple JWT

## Installation and Setup
1. Install the required packages:
   `pip install -r requirements.txt`

2. Apply database migrations:
   `python manage.py migrate`

3. Start the development server:
   `python manage.py runserver`

4. Test the API using Postman.

## API Endpoints
- GET `/api/books/` — List books.
- POST `/api/books/` — Create a book.
- PATCH `/api/books/<id>/` — Update a book.
- DELETE `/api/books/<id>/` — Delete a book.
- POST `/api/login/` — Log in.
- GET `/api/profile/` — View user profile.

## Authentication
Use the access token returned by the login endpoint as a Bearer Token for protected requests.

## Testing
API requests were tested using Postman.
