from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('token/', view=TokenObtainPairView.as_view(), name='token_contain_pair'),
]
