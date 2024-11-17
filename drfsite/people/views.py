from rest_framework import generics, viewsets

from .models import People
from .serializers import PeopleSerializer


# class PeopleViewSet(viewsets.ModelViewSet):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer


class PeopleAPIListView(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class PeopleAPIUpdateView(generics.UpdateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class PeopleAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
