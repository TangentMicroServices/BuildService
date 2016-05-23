from django.contrib import admin
from api.models import *

class MetricInline(admin.TabularInline):
    model = Metric
    extra = 0

class BooleanMetricInline(admin.TabularInline):
    model = BooleanMetric
    extra = 0   

class BuildAdmin(admin.ModelAdmin):
    inlines = [MetricInline, BooleanMetricInline]

admin.site.register(Metric)
admin.site.register(Smell)
admin.site.register(Project)
admin.site.register(Repo)
admin.site.register(Build, BuildAdmin)
