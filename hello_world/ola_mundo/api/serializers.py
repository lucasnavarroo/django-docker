from rest_framework.serializers import ModelSerializer
from ola_mundo.models import OlaMundo

class OlaMundoSerializer(ModelSerializer):
    class Meta:
        model = OlaMundo
        fields = [ 'nome']