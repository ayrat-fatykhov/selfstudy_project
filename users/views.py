from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """
    Создает Пользователя.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """
        Сохраняет пароль в закрытом виде.
        """
        user = serializer.save()
        user.set_password(user.password)
        user.save()
