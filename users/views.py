from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from users.models import User
from .serializer import UserSerializer
from django.contrib.auth.hashers import make_password

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