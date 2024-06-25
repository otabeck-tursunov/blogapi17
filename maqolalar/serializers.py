from rest_framework import serializers
from .models import Maqola


class MaqolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maqola
        fields = '__all__'
