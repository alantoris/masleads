from rest_framework import routers
from .views import ElementsViewSet
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r"elements", ElementsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
