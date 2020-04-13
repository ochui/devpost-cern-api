from django.urls import path
from api.views import ResourceListAPIView

urlpatterns = [
    path('resources', ResourceListAPIView.as_view()),
    path('markets', ResourceListAPIView.as_view()),
    path('stores', ResourceListAPIView.as_view()),
    path('pharmacies', ResourceListAPIView.as_view()),
]
