from rest_framework import serializers

from services._shared.serializer import BaseSerializer

from .models import Group, User
from .tasks import set_user_password_task


class SignupSerializer(BaseSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data) -> User:
        user = User.objects.create(
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            username=validated_data['username'],
            email=validated_data.get('email')
        )

        set_user_password_task.delay(str(user.guid), validated_data['password'])
        user.groups.add(Group.objects.filter(name='CUSTOMER').first())

        return user
    
    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('A user with that email already exists.')
        
        return email


class UserSerializer(BaseSerializer):
    class Meta:
        model = User
        exclude = ('password', 'user_permissions', 'is_active', 'is_deleted', 'is_staff', 'is_superuser')
