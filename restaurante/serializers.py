from dataclasses import fields
from rest_framework import serializers
from rest_framework import serializers
from restaurante.models import Prato

class PratoSerializer(serializers.ModelSerializer):

    class Meta:
        models = Prato
        fields = '__all__'