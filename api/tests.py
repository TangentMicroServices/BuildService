from django.test import TestCase, Client
from django.contrib.auth.models import User, AnonymousUser
from django.core.urlresolvers import reverse
from django.db import DatabaseError
import json
from mock import patch
from rest_framework.test import APIClient

class HealthTestCase(TestCase):
    def setUp(self):
        self.c = APIClient()
        self.status_fields = ['db', 'status']

    def test_health_endpoint_ok(self):
        url = reverse('health-list')
        response = self.c.get(url)
        assert response.status_code == 200, \
            "Expect 200 OK. got: {}" . format (response.status_code)

        expected_fields = ["db", "status"]

        for field in self.status_fields:
            assert response.json().get("status", {}).get(field, None) == "up", \
                "Expected field {} to exist" . format (field)

    @patch.object(User.objects, 'first')
    def test_determine_db_status(self, mock_query):
        """Health should not be ok if it cannot connect to the db"""

        mock_query.side_effect = DatabaseError()
        url = reverse('health-list')
        response = self.c.get(url)

        status = response.json().get("status", {})
        db_status = status.get('db')
        assert db_status == 'down', \
            'Expect DB to be down. Got: {}' . format (db_status)

        status = status.get('status')        
        assert status == 'down', \
            'Expect status to be down. Got: {}' . format (status)
        

