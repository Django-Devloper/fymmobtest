
from rest_framework.routers import DefaultRouter
from django.urls import path ,include
from . import views
router= DefaultRouter()
router.register('crud',views.CustomerViewSet,basename='Customer')

urlpatterns = [
    path('', include(router.urls)),

    ]
