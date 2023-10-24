from rest_framework import viewsets, mixins
from .models import ElementsToProcess
from .serializers import ElementsSerializer
from django_filters import rest_framework as filters
from .filters import ElementsFilter


class ElementsViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Viewset for retriving the list of elements and create new one,
    Aditionals filtering by status in the list
    """
    
    queryset = ElementsToProcess.objects.all()
    serializer_class = ElementsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ElementsFilter

