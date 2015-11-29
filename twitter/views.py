from rest_framework.views import APIView
from django.http import Http404
from django.http import JsonResponse

from albums.models import Photo, Album
from users.models import User

from twitter.scraper import TwitterScraper
from django.conf import settings

class ScraperTest(APIView):
    def get(self, request, format=None):
        scraper = TwitterScraper(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
        query = {
            'q': '#carnival',
            'filter': 'images',
            'include_entities': 'true'
        }
        data = {
            "photo_count": -1,
            "photo_limit": -1
        }
        # Get or Create Album
        album, created = Album.objects.get_or_create(name='carnival')
        
        # Get Last Photo Fetched
        try:
            photo = Photo.objects.filter(album=album).order_by('tweet_id').first()
            query['max_id'] = photo.tweet_id
        except:
            pass 
        
        # Get limit to know when to send email
        data['photo_count'] = Photo.objects.filter(album=album).count()
        if data['photo_count'] < 501:
            send_email_when = [100, 200, 300, 400, 500]
            find_limit = False
            i = 0
            while(not find_limit and i < len(send_email_when)):
                if data['photo_count'] < send_email_when[i]:
                    data['photo_limit'] = send_email_when[i]
                    find_limit = True
                i += 1

        tweets = scraper.get_tweets(query)
        scraper.save_tweets(tweets, album, data)

        return JsonResponse({"tweets": tweets})