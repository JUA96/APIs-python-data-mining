# tweet api credentials
consumerKey = "rehHagu6gJho85oFtGVQzZpUa"
consumerSecret = "0ShQ8hJzPwSEOYiu0u1QLLD2jHYzJhzwJnyo2wpKyHrwjDPmBG"
accessToken = "305201900-4XI5uGsLucYjksazjaJO0h3hdvMKcgKe8mM1A968"
accessTokenSecret = "gEjlnSo8Tvp1QvuBiHbLW1AClibzrAu4zXR9mQkxfHz3S"

# How to pass consumer key and consumer secret as the parameters
auth = OAuthHandler(consumer_key = consumerKey, consumer_secret = consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = API(auth)