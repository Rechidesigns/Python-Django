from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    product_list = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category_detail = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = "__all__"

