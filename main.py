from flask import Flask, render_template, redirect, url_for, session
from flask_bootstrap import Bootstrap5
from forms import CafeForm
import csv
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv',"a", newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            new_entry = [form.cafe.data,
                         form.location.data,
                         form.open_time.data.strftime("%I:%M %p"),
                         form.closing_time.data.strftime("%I:%M %p"),
                         form.coffee_rating.data,
                         form.wifi_rating.data,
                         form.power_outlet_rating.data
                         ]
            writer.writerow(new_entry)
        session['submitted'] = True #create a session stamp to know that the user submitted something
        return redirect(url_for('form_submitted'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        #newline ensures that python does not translate any linebreaks added
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = [row for row in csv_data]
    return render_template('cafes.html', cafes=list_of_rows)

@app.route('/form_submitted')
def form_submitted():
    # pop clears the stamp so the page can only be seen once after submitting
    return render_template('form_submitted.html', submit = session.pop('submitted',False))


if __name__ == '__main__':
    app.run(debug=True)
