from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token  # required for the check

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # ✅ ensures CharField exists

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')

    def create(self, validated_data):
        # ✅ ensures get_user_model().objects.create_user() is used
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        # Create a token for the new user
        Token.objects.create(user=user)
        return user
