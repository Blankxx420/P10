# P8: Pur Beurre
[Trello](https://trello.com/b/peua5jJ1/p8) <br>
Program only available in French now.

***How to use it***

👉[Click here to try it](https://healtyfoodchoice.herokuapp.com/)👈<br>
Create an account<br>
Search for a product<br>
Search for a substitute<br>
Save it as a favorite one

### Context
This is a web app to help you find a healthier substitute of a product you like eating. 😋

This project is part of my training at [Openclassrooms](https://openclassrooms.com/fr/) and the data is from the [OpenFoodFacts](https://fr.openfoodfacts.org/) REST API.

### Installation and configuration 💻
- Install packages with pipenv : `pipenv install`
_If you need to install pipenv : (with pip for Linux) `pip3 install pipenv` (with brew on Mac) `brew install pipenv` <br>
- Create your own .env file that will be used by [dotenv](https://pypi.org/project/python-dotenv/) library
- Create a superuser : `python3 manage.py createsuperuser`
- `createdb <db_name>`
- Check the database PORT
- Launch the migration : `python3 manage.py migrate`
- Launch the command that feeds the database : `python3 manage.py feed_db`


**Clone the repository from Github by running this command:**

`git clone https://github.com/Blankxx420/P8-Healty-choice.git`

**Execute with a virtual environment:**
Create a virtual environment: `pipenv shell` <br>
_If you need to install pipenv : (with pip for Linux) `pip3 install pipenv` (with brew on Mac) `brew install pipenv` <br>
Activate the virtual environment: `pipenv install` or `source venv/bin/activate` <br>

Run the application: `python3 manage.py runserver` and go to your localhost : `http://127.0.0.1:8000/`

(To deactivate the virtual environment, run this command: `exit`)

### Features 📋
+ Authentication
+ Research of a product and find a healthier substitute
+ Save substitutes as favorites

### Checklist 📝
- [x] Download postgreSQL, added django + psycopg2 + libpq-dev
- [x] Initialize django project
- [x] Modify default settings
- [x] Create templates folder for templates organization
- [x] Create base.html template
- [x] Create the search app
- [x] Create home.html template
- [x] Create users app
- [x] Create register.html template/view + add to urls
- [x] Create auth.html template/view + add to urls
- [x] Create models for products, categories and favorites
- [x] Download data from OpenFoodFacts API
- [x] Create database and insert data into it
- [x] Create products view (result of product research) + tests
- [x] Create product detail view + tests
- [x] Create algo to find substitutes (in substitutes' view)
- [x] Create substitutes view
- [x] Create feature to save favorite product-substitute
- [x] Create page that displays favorites
- [x] Create legal page
- [x] Added a functional test with Selenium
- [x] Add docstrings if needed
- [x] Check PEP8 with flake8 and refacto with black + manually
- [x] Deploy

### Tests 🧪
- Launches the unit tests : `coverage run --source='.' manage.py test`
- Display the coverage report : `coverage report`
- Display the html coverage report details : `coverage html`
- Launches the functional test with Selenium : `./manage.py test tests.users.functional_tests`
### Ressources used to create this program 🔧
***BACK***
- Language : Python 3.8
- Framework : Django
- Testing library : [pytest](https://docs.pytest.org/en/stable/getting-started.html), [coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/)
- HTTP library : [requests](https://docs.python-requests.org/en/master/)
- Progression bar library : [progress](https://pypi.org/project/progress/)

***FRONT***
- Languages : Javascript, HTML5 & CSS3
- Frameworks : Bootstrap 4

***EXTERNAL RESSOURCES***
- Web server /  HTTP server : [Gunicorn](https://gunicorn.org/)
- REST API : [OpenFoodFacts](https://fr.openfoodfacts.org/)

### Author 📝
[BRICE GUICHOU](https://github.com/Blankxx420)