⚙️ Steps to Run the Project

- cd blog_project
- python -m venv venv
- venv\Scripts\activate
- pip install django psycopg2-binary django-tailwind
- update settings.py (add your DB credentials)
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py tailwind install
- python manage.py tailwind start (keep this running in a separate terminal)
- python manage.py runserver
