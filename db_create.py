#!flask/bin/python
from migrate.versioning import api
from seminars.config import (SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
from seminars import app, db
import os.path
with app.app_context():
    db.create_all()

from seminars.models import Seminar

# Find the next seminar time.
import datetime as dt
next_slot = dt.datetime.strptime("Wednesday 12:00 PM", "%A %I:%M %p")
while next_slot < dt.datetime.now():
    next_slot += dt.timedelta(days=7)

for i in range(10):
    db.session.add(Seminar(start_datetime=next_slot))
    next_slot += dt.timedelta(days=7)

db.session.commit()

if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
