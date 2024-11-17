from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import People
from .permissions import IsAdminOrReadOnly
from .serializers import PeopleSerializer


# class PeopleViewSet(viewsets.ModelViewSet):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer


class PeopleAPIListView(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsAdminOrReadOnly,)


class PeopleAPIUpdateView(generics.UpdateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class PeopleAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsAdminOrReadOnly,)
