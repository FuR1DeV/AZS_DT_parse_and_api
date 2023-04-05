from .models import Azs
from rest_framework import viewsets, permissions
from .serializers import AzsSerializer


class AzsViewSet(viewsets.ModelViewSet):
    """Queryset это наши объекты в базе данных
    и указываем класс сериалайзера"""
    queryset = Azs.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AzsSerializer

