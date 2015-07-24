from flask_wtf import Form
from wtforms import StringField, DateTimeField, IntegerField, HiddenField, SelectField
from wtforms.validators import DataRequired, Length
from pytz import common_timezones

def _timezones():
    return [(tz, tz) for tz in common_timezones][::-1]

appointment_times =[(t, str(t) + " minutes") for t in [15, 30, 45, 60]]

class NewAppointmentForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    phone_number = StringField('Phone number', validators=[DataRequired(), Length(min=6)])
    delta = SelectField('Notification time', choices=appointment_times, validators=[DataRequired()])
    time = DateTimeField('Appointment time', validators=[DataRequired()], format="%m-%d-%Y %I:%M%p")
    timezone = SelectField('Time zone', choices=_timezones(), validators=[DataRequired()])