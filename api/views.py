from rest_framework import viewsets
from .models import *
from .seriliazers import *
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Trips.objects.all()
    serializer_class = CustomerSerilizer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get','head']

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            user=self.request.user
        )

