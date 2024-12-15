from flask import Blueprint, render_template, redirect
from ..tweets import tweets as all_tweets
from ..forms.form import TweetForm
from datetime import date
from random import randint

tweets = Blueprint("tweets", __name__, url_prefix="/tweets")
print('inside the tweets BP', __name__)


@tweets.route('/feed')
def get_all_tweets():
    return render_template('feed.html', tweets=all_tweets)

@tweets.route('/new', methods=["GET", "POST"])
def add_new_tweet():
    tweet_form = TweetForm()

    if tweet_form.validate_on_submit():
        new_tweet = {
            "id": len(all_tweets) + 1,
            "author": tweet_form.data["author"],
            "tweet": tweet_form.data["tweet"],
            'date': date.today()
        }

        print(new_tweet)
        all_tweets.append(new_tweet)
        return redirect('/tweets/feed')


    if tweet_form.errors:
        print(tweet_form.errors)
        return render_template("new_tweet.html", form=tweet_form.errors)

    return render_template("new_tweet.html", form=tweet_form, errors=None)
