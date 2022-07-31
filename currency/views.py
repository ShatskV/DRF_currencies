from ast import keyword
from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken

from currency.paginations import CustomPagination

from .models import Currency
from .serializers import CurrencySerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    pagination_class = CustomPagination
    queryset = Currency.objects.all().order_by('name')
    serializer_class = CurrencySerializer


class CustomAuthToken(ObtainAuthToken):
    keyword = "Bearer"
