from rest_framework import serializers
from api.models import Build, Metric, BooleanMetric

class MetricSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Metric  

class BooleanMetricSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BooleanMetric        

class BuildSerializer(serializers.ModelSerializer):

    metrics = MetricSerializer(many=True, read_only=True)
    booleans = BooleanMetricSerializer(many=True, read_only=True)
    
    class Meta:
        model = Build
        fields = ('build_number', 'repo', 'metrics', 'booleans')
        depth = 2

    """
    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album

    build_number = serializers.CharField(max_length=200)
    project = serializers.CharField(max_length=200)
    repo = serializers.CharField(max_length=200)
    metrics = serializers.ListField(MetricSerializer())
    booleans = serializers.ListField()
    
    def create(self, validated_data):

        build_number = validated_data.get('build_number')
        project = validated_data.get('project')
        repo = validated_data.get('repo')            

        return Build.record(build_number, project, repo)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance
    """