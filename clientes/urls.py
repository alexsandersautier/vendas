from django.urls import path
from .views import ClientesView, ClienteView

urlpatterns = [
    path('', view=ClientesView.as_view(), name='clientes'),
    path('<int:pk>/', view=ClienteView.as_view(), name='cliente'),
]