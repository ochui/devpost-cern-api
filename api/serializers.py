from rest_framework import serializers
from api.models import Resource, ResourceManger


class ResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resource
        fields = (
            '__all__'
        )

        # read_only_fields = (
        #     'name', 'description'
        # )


class ResourceMangerSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResourceManger
        fields = (
            '__all__'
        )

        # read_only_fields = (
        #     'name', 'description'
        # )
