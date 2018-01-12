


#from flask_login import LoginManager
#from flask_openid import OpenID
#from flask_googlelogin import GoogleLogin

from app import app, db
from views import *
#lm = GoogleLogin(app)


#lm = LoginManager()
#lm.init_app(app)
#oid = OpenID(app, os.path.join(app.root_path, "tmp"))

if __name__ == "__main__":
    app.run()
