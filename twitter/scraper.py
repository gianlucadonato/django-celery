from twitter.client import TwitterClient
from albums.models import Photo, Album
from users.models import User
from albums.serializers import AlbumSerializer, PhotoSerializer
from users.serializers import UserSerializer

class TwitterScraper(object):
    
    def __init__(self, consumer_key, consumer_secret):
        self.twitter = TwitterClient(consumer_key, consumer_secret)

    def get_tweets(self, params):
        return self.twitter.request('search/tweets.json', params)

    def save_tweets(self, tweets, album, data):
        for idx, item in enumerate(tweets["statuses"]):
            print "==> Fetching Tweet", idx 

            if item["entities"].get("media"):
                try:
                    user = User.objects.get(twitter_id=item["user"]["id"])
                    print "Load User:", user
                except User.DoesNotExist:
                    user = UserSerializer(data = {
                        "twitter_id" : item["user"]["id"],
                        "username" : item["user"]["screen_name"],
                        "profile_image_url" : item["user"]["profile_image_url"]
                    })
                    if user.is_valid():
                        user = user.save()
                        print "User saved successfully!", user
                    else:
                        print "Error Saving User", user.errors
                        pass

                photo = PhotoSerializer(data={
                    "tweet_id" : item["id"],
                    "tweet_text" : item["text"],
                    "tweet_likes" : item["favorite_count"],
                    "image_url" : item["entities"]["media"][0]["media_url"],
                    "user": user.id,
                    "album": album.id
                })
                if photo.is_valid():
                    photo = photo.save()
                    if (data['photo_count'] + idx + 1) == data['photo_limit']:
                        # TODO: Send Email w/ worker job
                        print "!!!! ======= SEND EMAIL ========= !!!!"

                    print "Photo saved successfully!", photo.image_url
                else:
                    print "Error saving Photo -> ", photo.errors
                    pass
            else:
                print "MEDIA NOT FOUND! WTF?"
                print item["entities"]