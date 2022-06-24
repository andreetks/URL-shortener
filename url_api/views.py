from django.shortcuts import redirect, render
from rest_framework import viewsets
from .models import Url
from .serializers import UrlSerializer

# Create your views here.

class UrlViewSet(viewsets.ModelViewSet):

    queryset = Url.objects.all()
    serializer_class = UrlSerializer