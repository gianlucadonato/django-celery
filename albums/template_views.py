from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import render

from albums.models import Photo, Album
from albums.serializers import PhotoSerializer, AlbumSerializer

class AlbumView(APIView):
    def get_object(self, name):
        try:
            return Album.objects.get(name=name)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, name):
        album = self.get_object(name)
        try:
            photos = Photo.objects.filter(album=album).order_by('tweet_id')
            context = {'photos': photos}
            return render(request, 'album_view.html', context)
        except:
            raise Http404