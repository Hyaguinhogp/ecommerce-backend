from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ProductsListCreate, ProductsDetailView


urlpatterns = [
    path('products/', ProductsListCreate.as_view(), name='products-list-crate'),
    path('products/<uuid:pk>', ProductsDetailView.as_view(), name='products-detail')
]