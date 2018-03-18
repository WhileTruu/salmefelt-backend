from rest_framework import serializers
from .models import ProductImage, Product
from django.contrib.auth.models import User


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'owner', 'productId', 'image', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class ProductSerializer(serializers.ModelSerializer):
    productimages = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'owner', 'name_et', 'name_en', 'description_et', 'description_en', 'productimages')
        read_only_fields = ('date_created', 'date_modified')

class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'products')
