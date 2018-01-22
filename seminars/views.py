from flask import render_template, flash, redirect, g, session, url_for, request
from flask_login import current_user
from app import app, db, google
from flask.ext.wtf import Form
from wtforms.ext.appengine.db import model_form

from .forms import SuggestSpeakerForm
from .models import User, Speaker, Seminar

@app.route('/')
@app.route('/index')
def index():
    return render_template("template.html", title="MoCA seminar series")

@app.route("/faq")
def faq():
    return render_template("faq.html")


@app.route("/seminars")
def seminars():
    return render_template("seminars.html",
                           upcoming_seminars=db.session.query(Seminar).filter(Seminar.speaker_id > 0).limit(10),
                           unscheduled_seminar_blocks=db.session.query(Seminar).filter(Seminar.is_confirmed != True).limit(10))

@app.route("/speakers")
def speakers():
    return render_template("speakers.html", 
        title="Seminar speakers", 
        speakers=db.session.query(Speaker).order_by(Speaker.availability_end.asc()))

@app.route("/speaker/<int:user_id>")
def speaker_details(user_id):
    speaker = Speaker.query.filter_by(id=user_id).first()
    if speaker is not None:
        return render_template("speaker.html",
                               speaker=speaker)
    else:
        # TODO: handle this better
        return render_template("404.html")

@app.route("/speaker/<int:user_id>/book")
def book_speaker(user_id):
    speaker = Speaker.query.filter_by(id=user_id).first()
    if speaker is not None:
        # Get available seminars given constraints.
        seminar_slots = db.session.query(Seminar)\
                                  .filter(Seminar.speaker_confirmed is not True)\
                                  .filter(Seminar.start_datetime.between(
                                      speaker.availability_start, 
                                      speaker.availability_end))\
                                  .all()

        return render_template("book_speaker.html", speaker=speaker,
            seminar_slots=seminar_slots)
    else:
        # TODO: handle this better.
        return render_template("404.html")


@app.route("/speaker/<int:user_id>/edit")
def edit_speaker_details(user_id):

    #MyForm = model_form(Speaker, base_class=Form, db_session=db.session)
    speaker = Speaker.query.filter_by(id=user_id).first()
    form = SuggestSpeakerForm(obj=speaker)
    #form = MyForm(request.form, speaker)

    if form.validate_on_submit():
        form.populate_obj(speaker)
        speaker.put()
        flash("Speaker details updated")
        return redirect("/speaker/{:.0f}".format(user_id))

    return render_template("suggest_speaker.html", form=form,
        title="Edit speaker details")



@app.route("/seminar/<int:seminar_id>")
def seminar_details(seminar_id):
    seminar = Seminar.query.filter_by(id=seminar_id).first()
    speaker = Speaker.query.filter_by(id=seminar.speaker_id).first()

    if seminar is not None and speaker is not None:
        return render_template("seminar.html", seminar=seminar, speaker=speaker)
    elif seminar is not None and speaker is None:
        # Book a speaker
        return render_template("book_seminar.html", seminar=seminar)

    else:
        # TODO: handle this better
        return render_template("404.html")



@app.route("/suggest", methods=["GET", "POST"])
def suggest_speaker():
    form = SuggestSpeakerForm(request.form)
    if form.validate_on_submit():

        # Check that we don't have this speaker already.
        exists = Speaker.query.filter_by(email=form.email.data).first()
        if exists is not None:
            # TODO: handle this better.
            flash("Speaker already exists")
            return redirect("/speakers")

        # Create a Speaker instance from the form inputs.
        speaker = Speaker(
            first_name=form.first_name.data.title(),
            last_name=form.last_name.data.title(),
            email=form.email.data,
            gender=form.gender.data,
            institution=form.institution.data.title(),
            personal_url=form.personal_url.data,
            availability_start=form.availability_start.data,
            availability_end=form.availability_end.data,
            has_already_scheduled_visit=form.has_already_scheduled_visit.data,
            host_full_name=form.host_full_name.data,
            host_email=form.host_email.data,
        )

        db.session.add(speaker)
        db.session.commit()
        flash("Speaker suggested")

        return redirect("/speakers")

    print("DID NOT VALIDATE")
    print(form.errors)
    print(form.availability_start)
    print(form.availability_start.data)

    return render_template(
        "suggest_speaker.html", form=form,
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