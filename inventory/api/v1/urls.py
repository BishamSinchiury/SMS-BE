from django.urls import path, include
from inventory.api.v1.routers import urlpatterns

urlpatterns = [
    path('inventory/', include(urlpatterns)),
]