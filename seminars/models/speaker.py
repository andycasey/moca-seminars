from ..app import db


class Speaker(db.Model):
    __tablename__ = "Speaker"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)

    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))

    gender = db.Column(db.String())

    #seniority/level?
    
    host_full_name = db.Column(db.String(120))
    host_email = db.Column(db.String(120))

    institution = db.Column(db.String(120))

    personal_url = db.Column(db.String(120))

    notes = db.Column(db.String())

    short_bio = db.Column(db.String())

    has_already_scheduled_visit = db.Column(db.Boolean)
    availability_start = db.Column(db.DateTime(timezone=True))
    availability_end = db.Column(db.DateTime(timezone=True))

    suggested_by_user_id = db.Column(db.Integer)
