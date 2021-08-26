from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import viewsets

from lestvica.serializers import MunicipalitySerializer, SmallMunicipalitySerializer
from lestvica.models import Municipality

class CachableReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    @method_decorator(cache_page(60*30))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @method_decorator(cache_page(60*30))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class MunicipalityViewSet(CachableReadOnlyModelViewSet):
    """
    API endpoint that shows municipalities and their data.
    """
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer


class SmallMunicipalityViewSet(CachableReadOnlyModelViewSet):
    """
    API endpoint that shows municipalities and their data.
    """
    queryset = Municipality.objects.all()
    serializer_class = SmallMunicipalitySerializer
    pagination_class = None
