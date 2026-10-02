# Philippine Cafe Database

A Flask website that lists cafes in Makati with their coffee, wifi, and
power outlet ratings, so you can find a good place to work.

**Live site:** 

## Features
- Browse all cafes in a table, with a Google Maps link for each
- Add a new cafe through a validated form
- Confirmation page that can only be seen right after submitting

## Built with
* Python
* Flask and Flask-WTF / WTForms
* Bootstrap-Flask
* Jinja2
* gunicorn

Cafe data is stored in a CSV file.

## Run it locally
1. Clone the repo and create a virtual environment
2. `pip install -r requirements.txt`
3. Create a `.env` file with `SECRET_KEY=<any long random string>` (.env.example file given)
4. run `python main.py` and open the development server.

## Known limitations / next steps
- Cafes added through the form are saved to a CSV on the server's disk,
  which resets as I am only on the free Render service.
  - **Next step: move storage to a database with SQLAlchemy.**
- No login, so anyone can add a cafe. No edit or delete entries yet.
- Expansion beyond just Makati, will add more places into the database.