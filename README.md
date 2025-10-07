# Bookaccino
## Project Python Web Final - Bookaccino

#### Welcome to Bookaccino!
#### This is my final exam project assignment for the course “Python Web Framework” at SoftUni.

### Description
Bookaccino is a site for readers and book recommendations. Our mission is to help people find and share books they love.

### Running the project locally
```sh
# 1) create & activate venv
python3 -m venv .venv
source .venv/bin/activate

# 2) verify you're in the venv
which python
python -V
python -m pip -V

# 3) install deps from requirements.txt
#python -m pip install -U pip setuptools wheel
python -m pip install -r requirements.txt

# 4) check deps (dependencies) are good
python manage.py check

# 5) run
python manage.py migrate
python manage.py runserver
```

### Simplest Ways to Make the Best of Bookaccino:
1. Set up a profile on Bookaccino.
2. Add you favorite books.
3. Find book recommendations.
4. Rate books to get better recommendations.
5. Find awesome quotes.
6. Enjoy Bookaccino.

### Functionalities include:
* Login/Register
* View/Edit/Delete profile
* Create books
* View/Edit/Delete books
* View/Edit/Delete clients (staff users)

### Technologies:
* Python 3.9
* Django 4.0.3
* PotgreSQL
