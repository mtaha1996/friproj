from django.urls import path,include
from .views import show_nodes,create_node

map_url = [
    path('show/',show_nodes),
    path('create/',create_node),
]
