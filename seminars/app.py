from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_oauth import OAuth

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)

oauth = OAuth()

google = oauth.remote_app('google',
    base_url='https://www.google.com/accounts/',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    request_token_url=None,
    request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
                    'response_type': 'code'},
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_method='POST',
    access_token_params={'grant_type': 'authorization_code'},
    consumer_key=app.config["GOOGLE_CLIENT_ID"],
    consumer_secret=app.config["GOOGLE_CLIENT_SECRET"])