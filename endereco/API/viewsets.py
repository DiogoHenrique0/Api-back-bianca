from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from endereco.models import Endereco
from .serializers import EnderecoSerializer

class EnderecoViewSet(ModelViewSet):
    """

    """
    queryset = Endereco.objects.all()
    serializer_class= EnderecoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao')
    lookup_field = 'nome'