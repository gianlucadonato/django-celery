from rest_framework import serializers
from models import Album, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            'tweet_id', 'tweet_text', 'tweet_likes', 
            'image_url', 'created_at', 'user', 'album'
        )

    def create(self, validated_data):
        return Photo.objects.create(**validated_data)


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'name')
