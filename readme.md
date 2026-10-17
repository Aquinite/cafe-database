# Philippine Cafe Database

A Flask website that lists cafes in Makati with their coffee, wifi, and
power outlet ratings, so you can find a good place to work.

**Live site:** https://cafedatabase.onrender.com

## Features
- Browse all cafes in a table, with a Google Maps link for each
- Cafes are pulled from a SQL database hosted on Neon
- Add a new cafe through a validated form, including a custom validator for the cafe name that checks whether a cafe is already inside the database. 
- Confirmation page that can only be seen right after submitting

## Built with
* Python
* PostgreSQL hosted on Neon
* Flask-SQLAlchemy 
* Flask and Flask-WTF / WTForms
* Bootstrap-Flask
* Jinja2
* gunicorn

Cafe data is stored in a CSV file.

## Run it locally
1. Clone the repo and create a virtual environment
2. `pip install -r requirements.txt`
3. Create a `.env` file with `SECRET_KEY=<any long random string>`(.env.example file given)
4. Because this now incorporates SQLAlchemy, you will need to create a database (SQLIte can work) and establish a connection to it by adding the url in the .env file. 
5. run `python main.py` and open the development server.

## Known limitations / next steps
- Add support for cafe descriptions and images, as well as fix formatting of opening and closing time to be combined into one column. 
- Add support for cafes that run 24 hours and allow this information to be collected into the form and displayed into the website.
- Allow users to suggest edits and deletions of entries in the database through a form. 
- Expansion beyond just Makati, will add more places into the database.
