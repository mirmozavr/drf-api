from rest_framework import generics
from django.shortcuts import render
from .models import People
from .serializers import PeopleSerializer


class PeopleAPIView(generics.ListAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer