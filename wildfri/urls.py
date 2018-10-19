from django.contrib import admin
from django.urls import path,include
from account.api.urls import account_url
from map.api.urls import map_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include(account_url)),
    path('map/',include(map_url))
]
