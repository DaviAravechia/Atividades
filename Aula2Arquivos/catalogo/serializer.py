from rest_framework import serializers
from .models import Filme

class FilmeSerializer(serializers.models.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'