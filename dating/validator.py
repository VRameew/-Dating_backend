from rest_framework import serializers
from dating.models import CustomUser, Match


class CustomUserValidator(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
