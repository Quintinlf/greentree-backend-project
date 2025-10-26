from django.urls import path
from .views import ExtractionRecordListCreateView, ExtractionRecordDetailView

urlpatterns = [
    path('records/', ExtractionRecordListCreateView.as_view(), name='record-list'),
    path('records/<int:pk>/', ExtractionRecordDetailView.as_view(), name='record-detail'),
]