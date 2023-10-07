from django.shortcuts import render
from rest_framework import viewsets
from seekosApi.models import CustomUser
from seekosApi.serializers import UserSerializer
from django.contrib.auth.decorators import login_required
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer   
