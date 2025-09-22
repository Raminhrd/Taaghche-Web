from django.urls import path
from audiobook.views  import CategoryListCreate, CategoryRetrieveUpdateDestroy, AudioBookListCreate, AudioBookRetrieveUpdateDestroy, AudioBookOrderDetailView, AudioBookOrderListCreateView


urlpatterns = [
    path('create-list', AudioBookListCreate.as_view()),
    path('retrieve-update-destroy/<str:pk>', AudioBookRetrieveUpdateDestroy.as_view()),
    path('category-list-create', CategoryListCreate.as_view()),
    path('category-retrieve-update-destroy/<str:pk>', CategoryRetrieveUpdateDestroy.as_view()),
    path('order-list-create', AudioBookOrderListCreateView.as_view()),
    path('oder-item-detail/<str:pk>', AudioBookOrderDetailView.as_view()),
]