from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from albums.template_views import AlbumView

album_urls = [
    url(r'^/(?P<name>[0-9a-zA-Z_-]+)/photos$', AlbumView.as_view(), name='album-photos'),
]

urlpatterns = [
  url(r'^api/', include('eversnap_api.urls')),
  url(r'^admin/', include(admin.site.urls)),
  
  # TEMPLATE VIEWS
  url(r'^albums', include(album_urls)),
]