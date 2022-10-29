from rest_framework.routers import DefaultRouter
from django.urls import path ,include
from . import views
router= DefaultRouter()
router.register('',views.CustomerViewSet,basename='Customer')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', include('rest_framework.urls')),

    ]