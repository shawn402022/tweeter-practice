from flask  import Flask, render_template, request
from .config import Config
from .tweets import tweets
from .routes.tweets_routes import tweets as all_tweets


from random import randint

app=Flask(__name__)
print(__name__)

app.config.from_object(Config)
app.register_blueprint(routes.tweets_routes.tweets, url_prefix='/tweets')


@app.route('/')
def randomTweet():
    single_tweet = tweets[randint(0,4)]
    return render_template('index.html', tweet=single_tweet)
