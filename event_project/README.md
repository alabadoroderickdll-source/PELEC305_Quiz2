# Event Registration System

A Django event registration app with form validation.

## Project Structure

```
event_project/
├── manage.py
├── requirements.txt
├── event_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── events/
    ├── __init__.py
    ├── apps.py
    ├── admin.py
    ├── models.py        ← EventRegistration model
    ├── forms.py         ← ModelForm with custom validation
    ├── views.py         ← register & success views
    ├── urls.py
    └── templates/
        └── events/
            ├── register.html
            └── success.html
```

## Local Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run migrations
python manage.py makemigrations
python manage.py migrate

# 3. (Optional) Create superuser for admin panel
python manage.py createsuperuser

# 4. Run the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the registration form.

## Validation Rules

| Field     | Rule                          |
|-----------|-------------------------------|
| Full Name | At least 5 characters         |
| Email     | Must end with `@gmail.com`    |
| Age       | Must be 18 or older           |
| Password  | At least 8 characters         |

## PythonAnywhere Deployment

1. Create a free account at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Open a Bash console and clone your GitHub repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   ```
3. Install dependencies:
   ```bash
   cd event_project
   pip install --user -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Go to **Web** tab → Add new web app → Manual configuration → Python 3.10
6. Set **Source code** path and **Working directory** to your project folder
7. In the **WSGI configuration file**, replace the contents with:
   ```python
   import os, sys
   path = '/home/YOUR_USERNAME/event_project'
   if path not in sys.path:
       sys.path.append(path)
   os.environ['DJANGO_SETTINGS_MODULE'] = 'event_project.settings'
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```
8. In `settings.py`, add your PythonAnywhere domain to `ALLOWED_HOSTS`:
   ```python
   ALLOWED_HOSTS = ['YOUR_USERNAME.pythonanywhere.com']
   ```
9. Reload the web app from the **Web** tab.
