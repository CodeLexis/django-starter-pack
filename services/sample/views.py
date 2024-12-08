from .models import Message

from services._shared.response import make_success_response
from services._shared.view import BaseView
from services.sample.serializers import MessageSerializer


class HelloView(BaseView):
    def get(self, request, *args, **kwargs):
        message = Message(content='Hello World')
        message_serializer = MessageSerializer(message)

        return make_success_response(data=message_serializer.data)

