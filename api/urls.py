from django.urls import path
from .views import (
    user_list_create_view, user_detail_view,
    category_list_create_view, category_detail_view,
    product_list_create_view, product_detail_view,
    order_list_create_view, order_detail_view,
    orderitem_list_create_view, orderitem_detail_view,
)

urlpatterns = [
    # User URLs
    path('users/', user_list_create_view, name='user_list_create'),
    path('users/<int:pk>/', user_detail_view, name='user_detail'),

    # Category URLs
    path('categories/', category_list_create_view, name='category_list_create'),
    path('categories/<int:pk>/', category_detail_view, name='category_detail'),

    # Product URLs
    path('products/', product_list_create_view, name='product_list_create'),
    path('products/<int:pk>/', product_detail_view, name='product_detail'),

    # Order URLs
    path('orders/', order_list_create_view, name='order_list_create'),
    path('orders/<int:pk>/', order_detail_view, name='order_detail'),

    # OrderItem URLs
    path('orderitems/', orderitem_list_create_view, name='orderitem_list_create'),
    path('orderitems/<int:pk>/', orderitem_detail_view, name='orderitem_detail'),
]

