from rest_framework import serializers
from .models import ExtractionRecord

class ExtractionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractionRecord
        fields = '__all__'  # includes name, value, created_at