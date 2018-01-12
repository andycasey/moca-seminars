from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField, SelectField
from wtforms.validators import DataRequired, Email, URL


class SuggestSpeakerForm(FlaskForm):

    first_name = StringField("first_name", validators=[DataRequired()])
    last_name = StringField("last_name", validators=[DataRequired()])
    
    email = StringField("email", validators=[DataRequired(), Email()])

    institution = StringField("institution", validators=[DataRequired()])

    #personal_url = StringField("personal_url",
    #                           validators=[URL(message="Invalid URL")])

    """

    gender = SelectField(
        "gender",
        validators=[DataRequired(
            message="This field is required for statistical purposes.")
        ],
        choices=("Prefer not to say", "Non-binary", "Female", "Male"))




    has_already_scheduled_visit = BooleanField(
        "has_already_scheduled_visit", validators=[DataRequired()])

    availability_start = DateTimeField(
        "availability_start",
        validators=[DataRequired(message=\
            "Speaker's availability is required for scheduling. "\
            "If availability is not known then use today as start date."
        )])

    availability_end = DateTimeField(
        "availability_end",
        validators=[DataRequired(message=\
            "Speaker's availability is required for scheduling. "\
            "If availability is not known then use end of calendar year as end date."
        )])

    """

    #notes = StringField("notes")
    #short_bio = StringField("short_bio")


