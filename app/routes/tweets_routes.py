from flask import Blueprint, render_template
from ..tweets import tweets as all_tweets

tweets = Blueprint("tweets", __name__, url_prefix="/tweets")
print('inside the tweets BP', __name__)


@tweets.route('/feed')
def get_all_tweets():
    #return 'all tweets'
    #for tweet in all_tweets:
        return render_template('feed.html', tweets=all_tweets)
