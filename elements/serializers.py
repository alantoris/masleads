from rest_framework import serializers
from .models import ElementsToProcess

class ElementsSerializer(serializers.ModelSerializer):
    """
    Generic serializers for Elements
    """

    class Meta:
        model = ElementsToProcess
        fields = "__all__"
