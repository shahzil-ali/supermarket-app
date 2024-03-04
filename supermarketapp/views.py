from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny



class MyUserViewset(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [AllowAny]

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
   
class SubcategoryViewset(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer  
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
 

class ItemViewset(viewsets.ModelViewSet):
    serializer_class = ItemSerializer 
    queryset = Item.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['subcategory']
    





