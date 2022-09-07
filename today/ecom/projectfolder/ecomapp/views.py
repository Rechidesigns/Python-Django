# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product
from .serializers import CategorySerializer
from .serializers import ProductSerializer
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

from rest_framework_simplejwt.authentication import JWTAuthentication
from account.permissions import IsAdminOrReadOnly

class CategoryView(APIView):
    """
    Retrive all or create new category instances
    """

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

    def get(self, request, format=None):
        """ Use this method to get all category instances"""

        objs = Category.objects.all() #get data
        serializers = CategorySerializer(objs, many=True)

        data = {
            "message" : "success",
            "data_count" : objs.count(),
            "data" : serializers.data
        }

        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(method= "post", request_body=CategorySerializer())
    @action(methods=["POST"], detail=True)
    def post(self, request, format=None):

            serializer = CategorySerializer(data=request.data)
            #get the data and deserialization

            if serializer.is_valid():
                serializer.save()

                data = {
                    "message" :"success"
                    }               
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                data = {
                    "message" :"failed",
                    "error" : serializer.error
                }

                return Response(data, status=status.HTTP_400_BAD_REQUEST)

        

class CategoryDetailView(APIView):
    """
    Retrive, update or delete a category instance..
    """

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

    def get_object(self, category_id):
        """"Get a single instance using the provided category_id""" 

        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise NotFound(detail = {"message", "Category not found"})
        
    def get(self, request, category_id, format=None):
        obj = self.get_object(category_id)
        serializer = CategorySerializer(obj)

        data = {
            "message" :"success"
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(method="put", request_body=CategorySerializer())
    @action(methods=["PUT"], detail=True)
    def put(self, request, Category_id, format=None):
        obj = self.get_object(Category_id)
        serializer = CategorySerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message" :"success"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "message" :"failed",
                "errors":serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(method="delete")
    @action(methods=["DELETE"], detail=True)
    def delete(self, request, category_id, formart=None):
        obj = self.get_object(category_id)
        if obj.products.count() == 0:

            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        raise PermissionDenied(detail={"message": "cannot delete this category because it contains live products."})



class ProductView(APIView):

    """
    Retrive all or create new category instances.
    """
    
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

    
    def get(self, request, format=None):

        objs = Product.objects.all() #get data
        serializers = ProductSerializer(objs, many=True)

        data = {
            "message" : "success",
            "data_count" : objs.count(),
            "data" : serializers.data
        }

        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(method="post", request_body=ProductSerializer())
    @action(methods=["POST"], detail=True)
    def post(self, request, format=None):

            serializer = ProductSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()

                data = {
                    "message" :"success"
                    }               
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                data = {
                    "message" :"failed",
                    "error" : serializer.error
                }

                return Response(data, status=status.HTTP_400_BAD_REQUEST)



    
class ProductDetailView(APIView):
    """
    Retrieve, update or delete a product instance
    """

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]
    
    def get_object(self, product_id):
        """Get a single product instance using the provided product_id"""
        try:
            return Product.objects.get(id = product_id)
        except Product.DoesNotExist:
            raise NotFound(detail = {"message": "Item not found"})
        
    def get(self, request, product_id, format=None):
        obj = self.get_object(product_id)
        serializer = ProductSerializer(obj)
        
        data = {
            "message":"success",
            "data": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


    @swagger_auto_schema(method="put", request_body=ProductSerializer())
    @action(methods=["PUT"], detail=True)
    def put(self, request, product_id, format=None):
        obj = self.get_object(product_id)
        serializer = ProductSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            
            data ={
                    "message" : "success",   
            }
            return Response(data, status=status.HTTP_201_CREATED)
          
        else:
            data ={
                    "message" : "Failed", 
                    "error": serializer.errors 
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(method="delete")
    @action(methods=["DELETE"], detail=True)   
    def delete(self, request, product_id, format=None):
        obj = self.get_object(product_id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)