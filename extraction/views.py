from rest_framework import generics
from .models import ExtractionRecord
from .serializers import ExtractionRecordSerializer

# List all records / create new record
class ExtractionRecordListCreateView(generics.ListCreateAPIView):
    queryset = ExtractionRecord.objects.all()
    serializer_class = ExtractionRecordSerializer

# Retrieve / update / delete a single record
class ExtractionRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExtractionRecord.objects.all()
    serializer_class = ExtractionRecordSerializer