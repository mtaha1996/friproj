from django.urls import path,include
from .views import signin

account_url = [
    path('login/',signin)
]
