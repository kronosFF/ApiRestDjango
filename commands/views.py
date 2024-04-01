from .models import Command
from rest_framework import generics
from .serializers import CommandSerializer

# Create your views here.
class CommandList(generics.ListCreateAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
    
class CommandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
