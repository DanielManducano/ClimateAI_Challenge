from django.contrib import admin
from .models import FlowData
from .models import PredictedValues
# Register your models here.

admin.site.register(FlowData)
admin.site.register(PredictedValues)