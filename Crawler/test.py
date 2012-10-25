import json
import urllib

fs_api = "https://api.foursquare.com/v2/users/%s/friends?oauth_token=53NL1UARTHYXIL3X1SAO4R4GZD0DGKBBGKQWR53MU2YJNZMP&v=20121025"
fs_user = "18568609"

fk_api = "http://api.flickr.com/services/rest/?method=flickr.contacts.getPublicList&api_key=71318b6fbd0a75b86300d5c205704f73&user_id=%s&format=json&nojsoncallback=1&auth_token=72157631853553817-523945a816220828&api_sig=fdb754733e193493377a9e89d3e8c0ee"
fk_user = "77565911@N00"
def test_crawler(url_fmt, user_id):
    url = url_fmt % (urllib.quote(user_id))
    data = urllib.urlopen(url).read()
    return json.loads(data)

    
