from django.urls import path 
from book.views import *


urlpatterns = [
    path('create-list', BookCreateList.as_view()),
    path('retrieve-update-delete/<str:pk>', BookRetrieveUpdateDestroy.as_view()),
    path('category-list-create', CategoryCreateList.as_view()),
    path('category-retrieve-update-delete/<str:pk>', CategoryRetrieveUpdateDestroy.as_view()),
]