from rest_framework import serializers
from .models import Cereal

class CerealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cereal
        fields = ['id', 'author', 'brand', 'created_at']
      