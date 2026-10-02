from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired(message="Field is required.")],
                       render_kw={"style": "max-width: 500px"})
    location = URLField('Google Maps link to location',
                        validators=[DataRequired(message="Field is required."), URL(message="Enter a valid Google Maps Link.")],
                        render_kw={"style": "max-width: 500px"})
    open_time = TimeField('Opening Time', validators=[DataRequired(message="Field is required.")],
                          render_kw={"style": "max-width: 500px"})
    closing_time = TimeField('Closing Time', validators=[DataRequired(message="Field is required.")],
                          render_kw={"style": "max-width: 500px"})
    coffee_rating = SelectField('Coffee rating (choose 1 coffee for lowest rating, 5 coffee highest)',
                                choices= ["☕️", "☕☕️️", "☕️️️️️️☕️️☕️", "☕️️️️️️☕️️️️️️☕️️️️☕️️️",
                                          "☕️️️️️️☕️️️️️️☕️️️️☕️☕️️️"],
                                validators=[DataRequired(message="Choice is required.")],
                                render_kw={"style": "max-width: 500px"})
    wifi_rating = SelectField('Wifi rating (choose X if no wifi, 1 bar lowest, 5 bar highest)',
                              choices=["❌", "🛜", "🛜🛜", "🛜🛜🛜", "🛜🛜🛜🛜️",
                                       "🛜🛜🛜🛜🛜️"],
                              validators=[DataRequired(message="Choice is required.")],
                              render_kw={"style": "max-width: 500px"})
    power_outlet_rating = SelectField('Power Outlet rating (choose X if no outlets, 1 plug lowest, 5 plug highest)',
                                      choices=["❌", "🔌️", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌️",
                                               "🔌🔌🔌🔌🔌"],
                                      validators=[DataRequired(message="Choice is required.")],
                                      render_kw={"style": "max-width: 500px"})
    submit = SubmitField('Submit')