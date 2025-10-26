from django.db import models

class ExtractionRecord(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

