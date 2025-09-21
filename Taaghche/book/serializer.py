from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from book.models import Category, Books, Order, OrderItem


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name', 'description']


class CategoryRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name', 'description']


class BookSerializer(ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Books
        fields = ['id', 'title', 'price', 'author', 'category','category_name', 'score', 'description']


class BookRetrieveUpdateDestroySerializer(ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Books
        fields = ['id', 'title', 'price', 'author', 'category','category_name', 'score', 'description']


class OrderTimeSerializer(ModelSerializer):
    product = BookSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']


class OrderSerializer(ModelSerializer):
    items = OrderTimeSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id','user', 'create_at', 'status', 'items']