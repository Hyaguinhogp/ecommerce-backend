from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.views import Response

from _core.permissions import IsAuthenticated
from users.models import User
from .serializers import UserSerializer, AuthSerializer

import jwt
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password, check_password

class UserView(ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def create(self, request, *args, **kwargs):
		p = request.data['password']
		request.data['password'] = make_password(p)
		return super().create(request, *args, **kwargs)

class UserDetailView(RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [IsAuthenticated]


class UserAuthView(APIView):
	def post(self, request, *args, **kwargs):
		serializer = AuthSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		password = serializer.validated_data['password']

		try:
			user = User.objects.get(email=serializer.validated_data['email'])
		except User.DoesNotExist:
			return Response({ 'response': 'Email ou senha inválidos'}, status=status.HTTP_400_BAD_REQUEST)
		
		if not user or not check_password(password, user.password):
			return Response({ 'response': 'Email ou senha inválidos'}, status=status.HTTP_400_BAD_REQUEST)
		
		token = self.generate_jwt_token(user)
		
		return Response({ 'token': token }, status=status.HTTP_200_OK)
	
	def generate_jwt_token(self, user):
		payload = {
			'user_id': str(user.id),
			'email': user.email,
			'exp': datetime.utcnow() + timedelta(days=1),
		}
		token = jwt.encode(payload, 'secret', algorithm='HS256')
		return token