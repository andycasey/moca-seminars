from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, URL, Required
from wtforms.fields.html5 import DateField
from datetime import  datetime

def today():
    return datetime.strftime(datetime.today(), "%Y-%m-%d")

def end_of_year():
    return datetime.strftime(datetime.today(), "%Y-12-31")


class RequiredIf(Required):
    def __init__(self, other_field_name, *args, **kwargs):
        self.other_field_name = other_field_name
        super(RequiredIf, self).__init__(*args, **kwargs)

    def __call__(self, form, field):
        other_field = form._fields.get(self.other_field_name)
        if other_field is None:
            raise Exception('no field named "%s" in form' % self.other_field_name)
        if bool(other_field.data):
            super(RequiredIf, self).__call__(form, field)


class SuggestSpeakerForm(FlaskForm):

    first_name = StringField("first_name", validators=[DataRequired()])
    last_name = StringField("last_name", validators=[DataRequired()])
    
    email = StringField("email", validators=[DataRequired(), Email()])

    institution = StringField("institution", validators=[DataRequired()])

    personal_url = StringField("personal_url",
                               validators=[])# TODO: URL(message="Invalid URL")])

    gender = SelectField(
        "gender",
        validators=[DataRequired(
            message="This field is required for statistical purposes.")
        ],
        choices=[
            ("female", "Female"),
            ("male", "Male"),
            ("non-binary", "Non-binary"),
        ])

    has_already_scheduled_visit = BooleanField("has_already_scheduled_visit")

    availability_start = DateField(
        "availability_start", format='%Y-%m-%d', default=today(),
        render_kw={'value': today()}
        )
    #validators=[DataRequired(message=\
    #        "Speaker's availability is required for scheduling. "\
    #        "If availability is not known then use today as start date."
    #    )])

    availability_end = DateField(
        "availability_end", format="%Y-%m-%d", default=end_of_year(),
        render_kw={"value": end_of_year()},
        validators=[RequiredIf("has_already_scheduled_visit")])

    #validators=[DataRequired(message=\
    #        "Speaker's availability is required for scheduling. "\
    #        "If availability is not known then use end of calendar year as end date."
    #    )])

    def validate_availability_start(form, field):
    
        return None
