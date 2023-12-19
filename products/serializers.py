from rest_framework import serializers

from .models import Category, Brands, Products

 
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['name']
        

class BrandsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brands
        fields = ['name']
        
    
class ProductsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandsSerializer()
    og_value = serializers.DecimalField(max_digits=10, decimal_places=3, read_only=True)
    discounted_price = serializers.DecimalField(max_digits=10, decimal_places=3, read_only=True)
    promotion = serializers.SerializerMethodField()
    
    class Meta:
        model = Products
        fields = [
            'id',
            'name',
            'category',
            'price',
            'brand',
            'promotion',
            'og_value',
            'discounted_price'
        ]
        
    def get_promotion(self, obj):
        return obj.brand.name == 'Adidas'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)

        if data.get('promotion'):
            og_value = instance.price
            discounted_price = self.calculate_promotion(og_value)
            data['og_value'] = og_value
            data['discounted_price'] = discounted_price
            
        return data
    
    def calculate_promotion(self, og_value):
        return round(og_value * 0.7, 2)