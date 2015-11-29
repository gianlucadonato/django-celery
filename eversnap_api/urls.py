from django.conf.urls import include, url
from albums.api_views import AlbumView, AlbumDetail, AlbumList
from twitter.views import ScraperTest

album_urls = [
    url(r'^/(?P<name>[0-9a-zA-Z_-]+)/photos$', AlbumView.as_view(), name='album-photos'),
    url(r'^/(?P<name>[0-9a-zA-Z_-]+)$', AlbumDetail.as_view(), name='album-detail'),
    url(r'^$', AlbumList.as_view(), name='album-list'),
]

urlpatterns = [
    url(r'albums', include(album_urls)),
    url(r'^twitter$', ScraperTest.as_view(), name='tweet-test')
]