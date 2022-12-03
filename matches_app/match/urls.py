from django.urls import path, include
from rest_framework import routers

from .views import MatchViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'matches', MatchViewSet)

urlpatterns = [
    path('', include(router.urls))
]