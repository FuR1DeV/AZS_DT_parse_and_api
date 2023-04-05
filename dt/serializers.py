from rest_framework import serializers
from .models import Azs


class AzsSerializer(serializers.ModelSerializer):
    """Сериализовываем нашу модель в JSON представлении"""
    class Meta:
        model = Azs
        fields = "__all__"
