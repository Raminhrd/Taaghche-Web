from django.shortcuts import render
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from audiobook.models import AudioBook, Category, AudioBookOrder, AudioBookOrderItem
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from audiobook.serializer import AudioBookSerializer, AudioBookRetrieveUpdateDestroySerializer, CategorySerializer, CategoryRetrieveUpdateDestroySerializer, AudioBookOrderSerializer, AudioBookOrderTimeSerializer



class CategoryListCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']


class CategoryRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryRetrieveUpdateDestroySerializer


class AudioBookListCreate(ListCreateAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['title']
    ordering_fields = ['price', 'score']


class AudioBookRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookRetrieveUpdateDestroySerializer



class AudioBookOrderListCreateView(ListCreateAPIView):
    queryset = AudioBookOrder.objects.all()
    serializer_class = AudioBookOrderSerializer


class AudioBookOrderDetailView(RetrieveUpdateAPIView):
    queryset = AudioBookOrder.objects.all()
    serializer_class = AudioBookOrderSerializer