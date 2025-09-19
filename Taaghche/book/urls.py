from django.urls import path 
from book.views import *


urlpatterns = [
    path('category-list-create', CategoryCreateList.as_view()),
]