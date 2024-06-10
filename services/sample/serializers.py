# Add serializers here

from services._shared.serializer import BaseSerializer

from .models import Message


class MessageSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Message
        exclude = (*BaseSerializer.Meta.exclude,)
