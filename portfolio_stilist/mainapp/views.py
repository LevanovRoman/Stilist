# from django.shortcuts import render
# from rest_framework import generics
from rest_framework import viewsets

from .models import *
from .serializers import *


# class BlogAPIView(generics.ListAPIView):
#     queryset = BlogModel.objects.all()
#     serializer_class = BlogSerializer

class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer


class ServicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServicesModel.objects.all()
    serializer_class = ServicesSerializer


class FeedbackViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FeedbackModel.objects.all()
    serializer_class = FeedbackSerializer


class PortfolioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PortfolioModel.objects.all()
    serializer_class = PortfolioSerializer




