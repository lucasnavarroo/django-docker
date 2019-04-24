from rest_framework.viewsets import ModelViewSet
from ola_mundo.models import OlaMundo
from .serializers import OlaMundoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class OlaMundoViewSet(ModelViewSet):
    queryset = OlaMundo.objects.all()
    serializer_class = OlaMundoSerializer
    # filter_backends = (DjangoFilterBackend)
    # filter_fields = ('nome')