
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from rest_framework import viewsets
from .serializers import ArticleSerializer
from .models import Article 

def index(request):
    
    return render(request,"blogger/templates/index.html")



class BloggerView(viewsets.ModelViewSet):
  	serializer_class = ArticleSerializer
  	queryset = Article.objects.all()   