from django.contrib.auth.models import Group, User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import SummarizeText


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'username', 'password', ]
        extra_kwargs = { 'password': {'write_only': True, 'required': True} }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user 
    
  
class SummarizeTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummarizeText
        fields = ['id', 'text', 'summary', 'created_at', 'updated_at', 'created_by']
        extra_kwargs = { 'summary': {'read_only': True} }
        
    def create(self, validated_data):
        return SummarizeText.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance