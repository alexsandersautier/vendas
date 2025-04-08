from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UsuariosView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UsuarioView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer