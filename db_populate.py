# Create seminar slots for the current year.
from seminars import db
from seminars.models import Seminar
for i in range(10):
    db.session.add(Seminar())
db.session.commit()
