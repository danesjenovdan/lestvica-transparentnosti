from django.urls import include, path
from rest_framework import routers
from lestvica import views

router = routers.DefaultRouter()
router.register(r'obcine', views.MunicipalityViewSet, basename='obcine')
router.register(r'obcine-mini', views.SmallMunicipalityViewSet, basename='obcine-mini')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
