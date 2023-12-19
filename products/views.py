from rest_framework import generics
from django_filters import rest_framework as filters

from _core.permissions import IsAuthenticated
from .models import Products
from .serializers import ProductsSerializer
from .filters import ProductsFilter


class ProductsListCreate(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductsFilter
    permission_classes = [IsAuthenticated]

    
class ProductsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticated]