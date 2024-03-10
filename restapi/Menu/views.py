from django.shortcuts import render
from rest_framework.response import Response
from Menu.models import Menu
from Menu.serializers import MenuSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from django.db.models import Q
from Menu.serializers import UserSerializer
from Menu.models import RatingAndReview
from Menu.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

# @api_view(['GET','POST','DELETE'])
# def Menulist(request):
#     if(request.method=="GET"):
#         menus=Menu.objects.all()
#         m=MenuSerializer(menus,many=True)
#         return Response(m.data)
#     elif(request=="POST"):
#
#         m=MenuSerializer(data=request.data)
#         if m.is_valid():
#             m.save()
#             return Response(m.data,status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#     elif(request=="DELETE"):
#         Menu.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET','PUT'])
# def MenuDetails(request,pk):
#     try:
#         menu=Menu.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if(request.method=="GET"):
#         m=MenuSerializer(menu)
#         return Response(m.data)
#     elif(request.method=="PUT"):
#         m=MenuSerializer(Menu,data=request.data)
#         if m.is_valid():
#             m.save()
#             return Response(m.data,status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
#

# Create your views here.

class Recipedetails(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class Reviewrating(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RatingAndReview.objects.all()
    serializer_class = ReviewSerializer


class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class search(APIView):
    def get(self, request):
        query = self.request.query_params.get('search')  # {paramas:{'search':'carrot'}} #default key search
        if (query):
            recipe = Menu.objects.filter(Q(name__icontains=query) | Q(ingredients__icontains=query))
            serialized_recipe = MenuSerializer(recipe, many=True)
            return Response(serialized_recipe.data)
        else:
            return Response([])

