from rest_framework import serializers
from api.models import Build, Metric, BooleanMetric, Repo, Project

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project 
        fields = ('name',)         

class RepositorySerializer(serializers.ModelSerializer):
    
    project = ProjectSerializer()
    class Meta:
        model = Repo 
        fields = ('name', 'project') 

class MetricSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Metric 
        fields = ('key', 'value', 'type') 

class BooleanMetricSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BooleanMetric 
        fields = ('key', 'value')        

class BuildSerializer(serializers.ModelSerializer):

    metrics = MetricSerializer(many=True)
    booleans = BooleanMetricSerializer(many=True)
    #project = serializers.CharField(max_length=200)
    repo = RepositorySerializer()    

    class Meta:
        model = Build
        fields = ('build_number', 'metrics', 'booleans', 'repo')
        depth = 2
    
    def create(self, validated_data):
        
        """
        {
         'build_number': 1, 
         'repo': OrderedDict([('name', 'repo'), ('project', OrderedDict([('name', 'project')]))]), 
         'metrics': [
            OrderedDict(
                [
                ('key', 'remediation'), 
                ('value', '100'), 
                ('type', 'default')])]
        }
        """

        build_number = validated_data.get('build_number')        
        repo_name = validated_data.get('repo').get('name')
        project_name = validated_data.get('repo').get('project').get('name')
        build = Build.record(build_number, project_name, repo_name)

        for metric in validated_data.get('metrics', []):  
           
            m = Metric(build=build)
            m.key = metric.get('key')
            m.value = metric.get('value')
            m.type = metric.get('type')
            m.save()

        for boolean in validated_data.get('booleans', []):
            b = BooleanMetric(build=build)
            b.key = boolean.get('key')
            b.value = boolean.get('value')
            b.save()

        return build

