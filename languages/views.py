from django.shortcuts import render
from .serializers import  LanguageSerializer,ParadigmSerializer,ProgrammerSerializer
from rest_framework import viewsets
from .models import  Language,Paradigm,Progammer
# Create your views here.

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Progammer.objects.all()
    serializer_class = ProgrammerSerializer
class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer