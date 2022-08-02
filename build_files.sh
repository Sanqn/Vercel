python3 -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install --upgrade pip
python3 manage.py collectstatic
python3 manage.py runserver