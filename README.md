# telemedicine_queue_django

Minimal Django project for a telemedicine queue API.

Requirements
- Python 3.11+
- See requirements.txt

Quick start (Windows cmd)
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Run tests
python manage.py test

Notes
- Do not commit virtualenv or __pycache__ (use .gitignore)