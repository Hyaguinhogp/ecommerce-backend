from rest_framework import generics

from _core.permissions import IsAuthenticated
from .models import Products
from .serializers import ProductsSerializers


class ProductsListCreate(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    permission_classes = [IsAuthenticated]

    
class ProductsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    permission_classes = [IsAuthenticated]