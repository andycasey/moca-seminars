from app import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return "<User {}>".format(self.email)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)

        except NameError:
            return str(self.id)



class Speaker(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)

    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))

    gender = db.Column(db.String())

    #seniority/level?

    institution = db.Column(db.String(120))

    personal_url = db.Column(db.String(120))

    notes = db.Column(db.String())

    short_bio = db.Column(db.String())

    availability_start = db.Column(db.DateTime(timezone=True))
    availability_end = db.Column(db.DateTime(timezone=True))

    suggested_by_user_id = db.Column(db.Integer)



class Seminar(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    speaker_id = db.Column(db.Integer)
    speaker_confirmed = db.Column(db.Boolean)

    title = db.Column(db.String(90))
    abstract = db.Column(db.String())

    # room booking: where/is confirmed?
    # TODO
    location = db.String(90)

    # start/end time
    start_datetime = db.Column(db.DateTime(timezone=True), nullable=False)

    # accommodation booking?

    # flight booking?

    # catering booking?

    def is_confirmed(self):
        return (self.speaker_id > 0) and self.speaker_confirmed

