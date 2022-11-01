from rest_framework import generics
from restaurante.models import Prato
from restaurante.serializers import PratoSerializers

class PratoListView(generics.ListAPIView):
    queryset = Prato.objects.all()
    serializer_class = PratoSerializers