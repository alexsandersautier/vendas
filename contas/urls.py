from django.urls import path
from .views import UsuariosView, UsuarioView

urlpatterns = [
    path('', view=UsuariosView.as_view(), name='usuarios'),
    path('<int:pk>/', view=UsuarioView.as_view(), name='usuario'),
]