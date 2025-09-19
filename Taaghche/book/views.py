from django.shortcuts import render
from django.http import  JsonResponse, HttpResponse
from book.models import *
from book.serializer import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView



class CategoryCreateList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer