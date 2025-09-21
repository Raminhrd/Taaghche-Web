from rest_framework.serializers import ModelSerializer
from audiobook.models import Category, AudioBook, AudioBookOrder, AudioBookOrderItem



class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class CategoryRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class AudioBookSerializer(ModelSerializer):
    class Meta:
        model = AudioBook
        fields = ['id', 'title', 'price', 'authors', 'category', 'score', 'description']


class AudioBookRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = AudioBook
        fields = ['id', 'title', 'price', 'authors', 'category', 'score', 'description']


class AudioBookOrderTimeSerializer(ModelSerializer):
    product = AudioBookSerializer(read_only=True)
    
    class Meta:

        model = AudioBookOrderItem
        fields = ['id', 'product', 'quantity']


class AudioBookOrderSerializer(ModelSerializer):
    items = AudioBookOrderTimeSerializer(many=True, read_only=True)

    class Meta:
        model = AudioBookOrder
        fields = ['id','user', 'create_at', 'status', 'items']