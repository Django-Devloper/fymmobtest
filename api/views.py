from rest_framework import viewsets
from .models import *
from .seriliazers import *
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CustomerSerilizer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Trips.objects.filter(user=self.request.user)
