import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(basedir, "seminars.db"))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, "db_repository")
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True
SECRET_KEY = ""

GOOGLE_CLIENT_ID = ""
GOOGLE_CLIENT_SECRET = ""
