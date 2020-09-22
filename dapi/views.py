from django.shortcuts import render

from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('real_name')
    serializer_class = UserSerializer
