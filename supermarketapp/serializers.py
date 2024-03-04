from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import *


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [ 'id','name', 'price', 'subcategory' ]

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number")
        return value
    
        

class SubcategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True , read_only=True)

    class Meta:
        model = Subcategory
        fields = ['id', 'category' ,'name','items']

    def validate_name(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Name cannot contain digits")
        return value    


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True , read_only=True )

    class Meta:
        model = Category
        fields = [ 'id','name','subcategories']

    def validate(self, value):
        special_chars = set("!@#$%^&*()_+{}[];:'\"|\\,.<>?")
        data = value.get('name')
        errors = []

        for char in data:
            if char in special_chars:
                raise serializers.ValidationError(errors)
            return value    


class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ['username','name','password','confirm_password']

    def validate(self, data):
        password = data.get('password')    
        confirm_password = data.get('confirm_password')  

        if password != confirm_password:
            raise serializers.ValidationError("Password and Confirm password does not match")
        return data
    
    def validate_username(self, data):
        if MyUser.objects.filter(username=data).exists():
            raise serializers.ValidationError("username already exists")
        return data
    
    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        name = validated_data.pop('name')  
        user = MyUser.objects.create_user(username=username, password=password, name=name) 
        return user