from django.contrib import admin
from django.urls import path

from django.urls import path, include
from blog.models import Match
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['local', 'away', 'stadium', 'local_goals', 'away_goals']

# ViewSets define the view behavior.
class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'matches', MatchViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
