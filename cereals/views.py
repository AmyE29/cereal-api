
from .models import Cereal
from .serializers import CerealSerializer
from rest_framework import generics


# Create your views here.
class CerealList(generics.ListAPIView):
    queryset = Cereal.objects.all()
    serializer_class = CerealSerializer

class CerealDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cereal.objects.all()
    serializer_class = CerealSerializer