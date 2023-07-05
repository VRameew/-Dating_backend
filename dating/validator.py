from rest_framework import serializers
from dating.models import CustomUser, Match


class CustomUserValidator(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'avatar', 'gender',
                  'first_name', 'last_name', 'email']


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
