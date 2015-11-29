from rest_framework import serializers
from models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 
            'profile_image_url', 'twitter_id', 'created_at'
        )

    def create(self, validated_data):
        return User.objects.create(**validated_data)