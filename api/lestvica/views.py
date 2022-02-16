from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import viewsets

from lestvica.serializers import MunicipalitySerializer, SmallMunicipalitySerializer
from lestvica.models import Municipality


class CachableReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    @method_decorator(cache_page(60 * 60 * 24 * 356))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


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
