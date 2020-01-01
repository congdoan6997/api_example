from django.shortcuts import render
from .serializers import  LanguageSerializer
from rest_framework import viewsets
from .models import  Language
# Create your views here.

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer