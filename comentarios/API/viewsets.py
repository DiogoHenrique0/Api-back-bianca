from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from .serializers import ComentarioSerializer

class ComentarioViewSet(ModelViewSet):
    """

    """
    queryset = Comentario.objects.all()
    serializer_class= ComentarioSerializer
    filter_backends = (SearchFilter,)
    permission_classes = (IsAuthenticated,)
    search_fields = ('nome', 'descricao')
    lookup_field = 'nome'