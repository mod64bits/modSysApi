from rest_framework import viewsets

from .models import Fornecedor
from .serializers import FornecedorSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows fornecedores to be viewed or edited.
    """
    queryset = Fornecedor.objects.all().order_by('-created')
    serializer_class = FornecedorSerializer
