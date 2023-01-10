from . import views
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'cliente',views.ClienteViewSet, basename="Cliente")

urlpatterns = [
    path('', include(router.urls)),

]