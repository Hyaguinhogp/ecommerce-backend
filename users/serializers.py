from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'name', 'email', 'password')

class SuperUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'name', 'email', 'password', 'is_superuser')

class AuthSerializer(serializers.Serializer):
	email = serializers.EmailField(max_length=150)
	password = serializers.CharField(max_length=500)