from http.client import CREATED

from services._shared.response import make_success_response
from services._shared.view import BaseView, BaseViewSet

from .models import User
from .serializers import SignupSerializer, UserSerializer


class SignupView(BaseView):
    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)

        return make_success_response(status=CREATED)


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def retrieve(self, request, pk, *args, **kwargs):
        if pk == 'me':
            return make_success_response(UserSerializer(instance=request.user).data)

        return super().retrieve(request, *args, **kwargs)
