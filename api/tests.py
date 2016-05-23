from django.contrib.auth.models import User, AnonymousUser
from django.core.urlresolvers import reverse
from django.db import DatabaseError
import json
from mock import patch
from rest_framework.test import APIClient
from django.test import TestCase, Client

class BuildDetailsAPITestCase(TestCase):

    def setUp(self):
        self.c = Client()
        self.build = Build.record(1, 'project', 'repo', [], [])
        url = reverse("build-detail", args = (self.build.pk,))
        self.response = self.c.get(url)

    def test_retrieve_build_200_ok(self):
        
        assert self.response.status_code == 200

    def test_has_expected_fields(self):

        expected_fields = ['build_number', 'repo', 'metrics', 'booleans']

        for field in expected_fields:
            data = self.response.json()
            assert data.get(field, None) is not None, \
                'Expected {} to exist. Actual result: {}' . format (field, data)


class ListBuildsTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def list_builds(self):
        url = reverse("build-list")
        response = self.c.post(url)

        assert response.status_code == 200, \
            'Expected 200OK. Got: {}' . format (response.content)

class SuccessfullyCreateNewBuildTestCase(TestCase):

    def setUp(self):
        self.c = Client()    
        self.repo_name = "UserService"
        self.project_name = "Tangent MicroServices"
        data = {
            "build_number": 1,
            "repo": {
                "name": self.repo_name,
                "project": {
                    "name": self.project_name
                }
            },
            "metrics": [{
                "key": "remediation",
                "value": "100",
                "type": "default"
            },
            {
                "key": "issues",
                "value": "10",
                "type": "default"
            }],
            "booleans": [{
                "key": "build_passed",
                "value": True
            }]
        }
        url = reverse("build-list")
        self.response = self.c.post(url, data=json.dumps(data), content_type='application/json')

        self.build = Build.objects.get(build_number=1)

    def test_response_is_201_created(self):
        assert self.response.status_code == 201

    def test_create_build_creates_repository(self):
        
        assert self.build.repo.name == self.repo_name

    def test_create_build_creates_project(self):
        
        assert self.build.repo.project.name == self.project_name

    def test_metrics_are_recorded(self):
        
        assert self.build.metrics.count() == 2

    def test_creates_booleans(self):
        bool_count = self.build.booleans.count() 
        assert bool_count == 1, \
            'Expected 1 boolean. Got: {}' . format (bool_count)


from api.models import Project, Repo, Build

class BuildModelTestCase(TestCase):

    def test_unicode(self):

        build = Build.record(1, 'sample-project', 'sample-repo')
        print(build)


    def test_build_record(self):

        metrics = [
            ("metric.coverage", 78),
            ("metric.loc", 1234),
            ("metric.static_analysis_issues", 1),
        ]
        booleans = [
            ("boolean.build_status", True),
            ("boolean.tests_run", False),
            ("boolean.tests_passed", True),
            ("boolean.codeclimate_run", False),
        ]

        build = Build.record(1, 'sample-project', 'sample-repo', metrics, booleans)

        assert build.build_number == 1

        assert len(Project.objects.filter(name='sample-project')) == 1, \
            'Expect a new project to have been created'
        assert len(Repo.objects.filter(name='sample-repo')) == 1, \
            'Expect a new repo to have been created'            


from api.serializers import MetricSerializer, BuildSerializer

class BuildSerializerTestCase(TestCase):
    pass

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
        

