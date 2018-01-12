from flask import render_template, flash, redirect, g, session, url_for, request
from flask_login import current_user
from app import app, db, google

from .forms import SuggestSpeakerForm
from .models import User, Speaker

@app.route('/')
@app.route('/index')
@app.route("/seminars")
def index():
    return render_template("template.html", title="MoCA seminar series")


@app.route("/speakers")
def speakers():
    return render_template("speakers.html", title="Seminar speakers")



@app.route("/suggest", methods=["GET", "POST"])
def suggest_speaker():
    form = SuggestSpeakerForm(request.form)

    if form.validate_on_submit():

        # Create a Speaker instance from the form inputs.

        speaker = Speaker(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            institution=form.institution.data
        )

        print("Speaker {}".format(speaker))

        db.session.add(speaker)
        db.session.commit()
        flash("Speaker suggested")

        return redirect("/speakers")

    return render_template("suggest_speaker.html", form=form,
        title="Suggest a spaker")








"""
@app.route('/foo')
def foo():
    access_token = session.get('access_token')
    if access_token is None:
        return redirect(url_for('login'))
 
    access_token = access_token[0]
    from urllib2 import Request, urlopen, URLError
 
    headers = {'Authorization': 'OAuth '+access_token}
    req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                  None, headers)
    try:
        res = urlopen(req)
    except URLError as e:
        if e.code == 401:
            # Unauthorized - bad token
            session.pop('access_token', None)
            return redirect(url_for('login'))
        return res.read()
 
    return res.read()
 
 
@app.route('/login')
def login():
    callback=url_for('authorized', _external=True)
    return google.authorize(callback=callback)
 
 
 
@app.route("/oauth2callback")
@google.authorized_handler
def authorized(resp):
    access_token = resp['access_token']
    session['access_token'] = access_token, ''
    return redirect(url_for('index'))
 
 
@google.tokengetter
def get_access_token():
    return session.get('access_token')
"""