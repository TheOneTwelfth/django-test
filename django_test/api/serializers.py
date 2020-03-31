from rest_framework import serializers

from . import models


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.App
        fields = ('id', 'name', 'api_key')
        read_only_fields = ('id', 'api_key')
