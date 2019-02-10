from instagram.client import InstagramAPI

access_token ="7276625302.ad072d9.94b52704b09940bdb4e10b55eb92e512"
client_secret = "0d404a22dbc047a791dfafddce9395e9"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next_ = api.user_recent_media(user_id="userid", count=10)
for media in recent_media:
   print (media.caption.text)
