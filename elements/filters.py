from django_filters import rest_framework as filters
from .models import ElementsToProcess


class ElementsFilter(filters.FilterSet):
    """
    Class to generate a filter for endpoints related to Elements
    """
    status = filters.NumberFilter(field_name="status")

    class Meta:
        model = ElementsToProcess
        fields = ['status']
