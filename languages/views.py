from django.shortcuts import render
from rest_framework import viewsets
from .models import Language, Programmer, Paradigm
from .serializers import LanguageSerializer, ProgrammerSerializer, ParadigmSerializer


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
