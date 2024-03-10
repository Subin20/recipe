from rest_framework import serializers
from Menu.models import Menu
from Menu.models import RatingAndReview
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields=['id','name','cuisine','meal_type','ingredients','price','created_at','updated_at']



class ReviewSerializer(serializers.ModelSerializer):
    permission_classes=[IsAuthenticated]
    class Meta:
        model=RatingAndReview
        fields=['recipe_id','user','rating','comment','created_at','updated_at']


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['id','username','password']

    def create(self,validated_data):
        u=User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        u.save()
