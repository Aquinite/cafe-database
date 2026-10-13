from flask import Flask, render_template, redirect, url_for, session
from flask_bootstrap import Bootstrap5
from forms import CafeForm
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv
from models import db, Makati

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
bootstrap = Bootstrap5(app)

#Initialize the SQLAlchemy extension for the Flask app instance:
db.init_app(app)

#Create all tables if not yet created.
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_to_add = Makati(cafe_name= form.cafe.data,
             gmaps_location= form.location.data,
             days_open = form.days_open.data,
             opening_time= form.open_time.data,
             closing_time= form.closing_time.data,
             coffee_rating = form.coffee_rating.data,
             wifi_rating = form.wifi_rating.data,
             outlet_rating = form.power_outlet_rating.data)
        db.session.add(cafe_to_add)
        db.session.commit()
        session['submitted'] = True #create a session stamp to know that the user submitted something
        return redirect(url_for('form_submitted'))
    return render_template('add.html', form=form)

@app.errorhandler(SQLAlchemyError)
def error_handler(error):
    db.session.rollback()
    return render_template("error.html", error = error.message.detail)


@app.route('/cafes')
def cafes():
    all_cafes = db.session.execute(db.select(Makati)).scalars().all()
    column_names = [" ".join(c.name.split("_")).title() for c in Makati.__table__.columns]
    return render_template('cafes.html',cafes = all_cafes, column_names = column_names)


@app.route('/form_submitted')
def form_submitted():
    # pop clears the stamp so the page can only be seen once after submitting
    return render_template('form_submitted.html', submit = session.pop('submitted',False))


if __name__ == '__main__':
    app.run(debug=True)
