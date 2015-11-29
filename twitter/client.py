import requests
import base64

API_ENDPOINT = 'https://api.twitter.com'
API_VERSION = '1.1'
REQUEST_TOKEN_URL = '%s/oauth2/token' % API_ENDPOINT


class TwitterClient(object):
    """This class implements the Twitter's Application-only authentication."""

    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = ''

    def request(self, path, payload={}):
        """Send an authenticated request to the Twitter API."""
        if not self.access_token:
            self.access_token = self.get_access_token()

        url = '%s/%s/%s' % (API_ENDPOINT, API_VERSION, path)
        headers = {'Authorization': 'Bearer %s' % self.access_token }
        response = requests.get(url, headers=headers, params=payload)
        return response.json()

    def rate_limit_status(self, resource=''):
        """Returns a dict of rate limits by resource."""
        response = self.request('application/rate_limit_status.json', resource)
        if resource:
            r = resource.split('/')
            if len(r) > 1:
                return response['resources'][r[1]][resource]
            else:
                return response['resources'][r[1]]
        return response

    def get_access_token(self):
        """Obtain a bearer token."""
        bearer_token = '%s:%s' % (self.consumer_key, self.consumer_secret)
        encoded_bearer_token = base64.b64encode(bearer_token.encode('ascii'))
        headers = {
            'Authorization': 'Basic %s' % encoded_bearer_token.decode('utf-8'),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        payload = { 'grant_type': 'client_credentials' }
        response = requests.post(REQUEST_TOKEN_URL, params=payload, headers=headers)
        data = response.json()
        return data['access_token']
