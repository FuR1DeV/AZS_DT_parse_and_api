from rest_framework import serializers
from .models import Azs


class AzsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Azs
        fields = "__all__"
