from rest_framework import serializers
from .models import accounts

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = accounts
        fields = '__all__'

class DosyaSerializer(serializers.Serializer):
    file = serializers.FileField()