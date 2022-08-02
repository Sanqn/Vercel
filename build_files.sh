python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install --upgrade pip
python manage.py collectstatic
python manage.py runserver