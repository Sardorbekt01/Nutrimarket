from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Category, Product, Order, OrderItem
from .serializers import UserSerializer, CategorySerializer, ProductSerializer, OrderSerializer, OrderItemSerializer

# User views
@api_view(['GET', 'POST'])
def user_list_create_view(request):
    if request.method == 'GET':
        users = User.objects.all()
        if 'application/json' in request.headers.get('Accept', ''):
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        else:
            return render(request, 'user_list.html', {'users': users})
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    
    if request.method == 'GET':
        if 'application/json' in request.headers.get('Accept', ''):
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return render(request, 'user_detail.html', {'user': user})
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Category views
@api_view(['GET', 'POST'])
def category_list_create_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        if 'application/json' in request.headers.get('Accept', ''):
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)
        else:
            return render(request, 'category_list.html', {'categories': categories})
    
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'GET':
        if 'application/json' in request.headers.get('Accept', ''):
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        else:
            return render(request, 'category_detail.html', {'category': category})
    
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Product views
@api_view(['GET', 'POST'])
def product_list_create_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        if 'application/json' in request.headers.get('Accept', ''):
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        else:
            return render(request, 'product_list.html', {'products': products})
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'GET':
        if 'application/json' in request.headers.get('Accept', ''):
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        else:
            return render(request, 'product_detail.html', {'product': product})
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Order views
@api_view(['GET', 'POST'])
def order_list_create_view(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        if 'application/json' in request.headers.get('Accept', ''):
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)
        else:
            return render(request, 'order_list.html', {'orders': orders})
    
    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def order_detail_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    
    if request.method == 'GET':
        if 'application/json' in request.headers.get('Accept', ''):
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        else:
            return render(request, 'order_detail.html', {'order': order})
    
    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# OrderItem views
@api_view(['GET', 'POST'])
def orderitem_list_create_view(request):
    if request.method == 'GET':
        order_items = OrderItem.objects.all()
        if 'application/json' in request.headers.get('Accept', ''):
            serializer = OrderItemSerializer(order_items, many=True)
            return Response(serializer.data)
        else:
            return render(request, 'orderitem_list.html', {'order_items': order_items})
    
    elif request.method == 'POST':
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def orderitem_detail_view(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    
    if request.method == 'GET':
        if 'application/json' in request.headers.get('Accept', ''):
            serializer = OrderItemSerializer(order_item)
            return Response(serializer.data)
        else:
            return render(request, 'orderitem_detail.html', {'order_item': order_item})
    
    elif request.method == 'PUT':
        serializer = OrderItemSerializer(order_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        order_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
