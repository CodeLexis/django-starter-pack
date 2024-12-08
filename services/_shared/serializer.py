from rest_framework.serializers import ModelSerializer


class BaseSerializer(ModelSerializer):
    class Meta:
        exclude = ('is_deleted',)

    def to_representation(self, instance):
        result = super().to_representation(instance)

        if type(result) is dict:
            result = dict(sorted(result.items()))

        return result
