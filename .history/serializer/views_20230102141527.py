from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializer import CategorySerializer, LessonSerializer, ProductSerializer
from lesson.models import Lesson, Asset, Category, Instruction
from products.models import Products
from rest_framework import status
from django.db.models import Q

class LessonView(APIView):
    serializer_class = LessonSerializer
    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug", None)
        if slug:
            queryset = Lesson.objects.get(slug=slug)
            serializer = self.serializer_class(queryset)
            return Response(serializer.data)
            
        queryset = Lesson.objects.all().order_by("-created")
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class ProductListView(APIView):
    serializer_class = ProductSerializer
    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug", None)
        related = kwargs.get("related", None)
        if slug:
            try:
                queryset = Products.objects.get(slug=slug)
                serializer = self.serializer_class(queryset)  
                return Response(serializer.data)
            except Products.DoesNotExist:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        if related:
            try:
                queryset = Products.objects.get(slug__icontains="")
                print(queryset.category)
            except Products.DoesNotExist:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

            queryset = Products.objects.filter(category__name__icontains=queryset.category.name).exclude(slug=queryset.slug).order_by("-created",)
            if len(queryset) > 0:   
                serializer = self.serializer_class(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"data":None})
        
        queryset = Products.objects.all().order_by("-created",)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
    def get_queryset(self):
        queryset = Category.objects.all().order_by("-id")
        
        return queryset
    