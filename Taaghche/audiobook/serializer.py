from rest_framework.serializers import ModelSerializer
from audiobook.models import *



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
        fields = ['id', 'title', 'price', 'author', 'category', 'score', 'description']


class AudioBookRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = AudioBook
        fields = ['id', 'title', 'price', 'author', 'category', 'score', 'description']