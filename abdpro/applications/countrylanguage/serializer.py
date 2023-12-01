from rest_framework import serializers, pagination

from .models import(
    countrylanguage
)

class countrylanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = countrylanguage
        fields = ('__all__')
