
from rest_framework import serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView
from api.models import ResourceManger, Resource
from api.serializers import ResourceMangerSerializer, ResourceSerializer


class ResourceListAPIView(ListAPIView):

    serializer_class = ResourceSerializer
    filterset_fields = [
        'resource_type',
        'resource_status',
        'state', 'lga'
    ]

    def get_queryset(self):
        return Resource.objects.all()


class StoreListAPIView(ListAPIView):

    serializer_class = ResourceSerializer
    filterset_fields = [
        'resource_status', 'state', 'lga'
    ]

    def get_queryset(self):
        return Resource.objects.filter(resource_type=Resource.ResourceTypes.STORE)


class MarketListAPIView(ListAPIView):

    serializer_class = ResourceSerializer
    filterset_fields = [
        'resource_status', 'state', 'lga'
    ]

    def get_queryset(self):
        return Resource.objects.filter(resource_type=Resource.ResourceTypes.MARKET)


class PharmacyListAPIView(ListAPIView):

    serializer_class = ResourceSerializer
    filterset_fields = [
        'resource_status', 'state', 'lga'
    ]

    def get_queryset(self):
        return Resource.objects.filter(resource_type=Resource.ResourceTypes.PHARMACY)
