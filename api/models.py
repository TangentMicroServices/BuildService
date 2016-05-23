from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200, blank=False, null=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Repo(models.Model):

    def __str__(self):
        return self.name

    project = models.ForeignKey(Project)
    name = models.CharField(max_length=200, blank=False, null=False)

class Build(models.Model):    
    """
    curl -X POST /buidservice/{project}/ \
      -d metric.name=   
    """
    def __str__(self):
        return "{}.{}: #{}" . format (self.repo.project.name, self.repo.name, self.build_number)

    repo = models.ForeignKey(Repo)
    build_number = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    

    @staticmethod
    def record(build_number, project, repo, metrics=[], booleans=[], **kwargs):

        project, created = Project.objects.get_or_create(name=project)
        repo, created = Repo.objects.get_or_create(project=project, name=repo)

        build = Build()
        build.repo = repo
        build.build_number = build_number

        build.save()
        return build


class Smell(models.Model):
    check_name = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField()
    remediation = models.IntegerField()
    description = models.CharField(max_length=200, blank=False, null=False)
    issue_type = models.CharField(max_length=200, blank=False, null=False)
    engine = models.CharField(max_length=200, blank=False, null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class SmellCategories(models.Model):

    smell = models.ForeignKey(Smell)
    title = models.CharField(max_length=200, blank=False, null=False)

METRIC_TYPES = [
    ('default', None),
    ('percent', 'percent'),
]

class Metric(models.Model): 
    build = models.ForeignKey(Build, related_name='metrics')
    key = models.CharField(max_length=200, blank=False, null=False)
    value = models.CharField(max_length=200, blank=False, null=False)
    type = models.CharField(max_length=200, blank=False, null=True, choices=METRIC_TYPES, default=None)

class BooleanMetric(models.Model):  
    build = models.ForeignKey(Build, related_name='booleans') 
    key = models.CharField(max_length=200, blank=False, null=False)
    value = models.BooleanField(default=False)


