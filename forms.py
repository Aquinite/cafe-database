from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired, URL, ValidationError
from sqlalchemy import func
from models import db, Makati


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name (indicate branch if naming a multi-branch cafe)', validators=[DataRequired(message="Field is required.")],
                       render_kw={"style": "max-width: 500px"},
                       filters=[lambda x: " ".join(x.split()) if x else x]) #pass data into this filter in order to validate properly with the database
    location = URLField('Google Maps link to location',
                        validators=[DataRequired(message="Field is required."), URL(message="Enter a valid Google Maps Link.")],
                        render_kw={"style": "max-width: 500px"})
    days_open = StringField('Days Open (type "Everyday" for cafes that open everyday, '
                            'if with diff schedule please note down days they are open.) ',
                            validators=[DataRequired(message="Field is required.")],
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

    def validate_cafe(self, cafe):
        """Checks with the database if the cafe already exists."""
        cafe_field_data = cafe.data.replace(" ", "").lower() #removes all spaces from the field data for comparison
        cafe_to_validate = db.session.execute(
            db.select(Makati).where(func.lower(func.replace(Makati.cafe_name," ", "")) == cafe_field_data)).scalar()
        # also removes all the spaces from the database data to handle for inconsistent space data
        if cafe_to_validate is not None:
            raise ValidationError(f"{cafe.data} already exists in the database.")



