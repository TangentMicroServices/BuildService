from django.contrib.auth.models import User
from api.models import Build, Metric, Smell
from rest_framework import routers, serializers, viewsets, decorators, response
from api.permissions import IsSelfOrSuperUser
from api.serializers import BuildSerializer, MetricSerializer, SmellSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
# Serializers define the API representation.

class MetricViewSet(viewsets.ModelViewSet):
    
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer

class BuildViewSet(viewsets.ModelViewSet):
    
    queryset = Build.objects.all()
    serializer_class = BuildSerializer

class SmellViewSet(viewsets.ModelViewSet):
    
    queryset = Smell.objects.all()
    serializer_class = SmellSerializer    


class HealthViewSet(viewsets.ViewSet):

    permission_classes = (AllowAny, )

    def list(self, request, format=None):

        # make sure we can connect to the database
        all_statuses = []
        status = "up"

        db_status = self.__can_connect_to_db()

        all_statuses.append(db_status)

        if "down" in all_statuses:
            status = "down"

        data = {
            "data": {
                "explorer": "/api-explorer",
            },
            "status": {
                "db": db_status,
                "status": status
            }
        }
        return response.Response(data)

    def __can_connect_to_db(self):
        try:
            user = User.objects.first()
            return "up"
        except Exception:
            return "down"

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'health', HealthViewSet, base_name='health')
router.register(r'build', BuildViewSet, base_name='build')
router.register(r'metric', MetricViewSet, base_name='metric')
router.register(r'smell', SmellViewSet, base_name='smell')



"""
List all users.

**Notes:**

* Requires authenticated user

**Example usage:**

    import requests
    response = requests.get('/users/')

**Example response:**

    [
      {
        "url": "http://192.168.99.100:8000/users/1/",
        "username": "admin",
        "email": "a@b.com",
        "is_staff": true,
        "first_name": "",
        "last_name": ""
      }
    ]



---
responseMessages:
- code: 403
  message: Not authenticated

consumes:
    - application/json
produces:
    - application/json
"""