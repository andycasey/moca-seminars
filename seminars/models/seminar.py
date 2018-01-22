
from ..app import db
from sqlalchemy.orm import relationship, backref



class Seminar(db.Model):
    __tablename__ = "Seminar"

    id = db.Column(db.Integer, primary_key=True)

    speaker_id = db.Column(db.Integer, db.ForeignKey('Speaker.id'))
    speaker_confirmed = db.Column(db.Boolean, default=False)

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

    invitations = relationship("Invitation", secondary="seminar_invitations",
        backref=backref("Seminar"))

    def is_confirmed(self):
        return (self.speaker_id > 0) and self.speaker_confirmed


class Invitation(db.Model):
    __tablename__ = "Invitation"
    id = db.Column(db.String, primary_key=True)

    created = db.Column(db.DateTime)
    status = db.Column(db.String) # waiting / accepted / declined

    requested_seminar_id = db.Column(db.Integer)
    requested_accommodation = db.Column(db.String)
    requested_flights = db.Column(db.String)

    seminars = relationship("Seminar", secondary="seminar_invitations",
        backref=backref("Invitation"))


class SeminarInvitations(db.Model):
    __tablename__  = "seminar_invitations"
    id = db.Column(db.Integer, primary_key=True)
    seminar_id = db.Column(db.Integer, db.ForeignKey('Seminar.id'), primary_key=True)
    invitation_id = db.Column(db.Integer, db.ForeignKey('Invitation.id'), primary_key=True)

    #seminar = db.relationship(Seminar, backref=backref("SeminarInvitations", cascade="all, delete-orphan"))
    #invitation = db.relationship(Invitation, backref=backref("SeminarInvitations", cascade="all, delete-orphan"))
