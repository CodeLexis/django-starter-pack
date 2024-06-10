from rest_framework.serializers import ModelSerializer


class BaseSerializer(ModelSerializer):
    class Meta:
        exclude = ('is_deleted',)
