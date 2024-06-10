# Add serializers here

from services._shared.serializer import BaseSerializer

from .models import Message


class MessageSerializer(BaseSerializer):
    class Meta:
        model = Message
        fields = '__all__'
