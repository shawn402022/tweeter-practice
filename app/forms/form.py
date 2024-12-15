from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Length

class TweetForm(FlaskForm):
    author = StringField("Author", validators=[DataRequired(), Length(max=10, message='name cannot exceed 10 characters')])
    tweet = StringField("Tweet", validators=[DataRequired(),Length(max=20, message ="Tweets must not exceed 20 characters")])
    submit = SubmitField("Create Tweet")
