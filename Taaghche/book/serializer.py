from rest_framework.serializers import ModelSerializer
from book.models import *


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name', 'description']


class CategoryRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name', 'description']


class BookSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'price', 'author', 'category', 'score', 'description']


class BookRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'price', 'author', 'category', 'score', 'description']


class OrderTimeSerializer(ModelSerializer):
    class Meta:
        product = BookSerializer

        model = OrderItem
        fields = ['id', 'product', 'quantity']


class OrderSerializer(ModelSerializer):
    items = OrderTimeSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id','user', 'create_at', 'status', 'items']