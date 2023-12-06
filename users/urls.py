from django.urls import path
from . import views


urlpatterns = [
	path('users/', views.UserView.as_view()),
	path('users/<uuid:pk>/', views.UserDetailView.as_view()),
	path('auth/', views.UserAuthView.as_view()),
]