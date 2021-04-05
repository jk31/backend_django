# Backend with Django

## Requirements so far

* [Django](https://www.djangoproject.com/)
* [Django Heroku](https://devcenter.heroku.com/articles/django-app-configuration)
* [Django REST Framework](https://www.google.com)
* [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html)
* [Django CORS Headers](https://pypi.org/project/django-cors-headers/)

## Features

* Django 3 as base
* Ready for deployment on Heroku
* REST API
  * API keys (TODO)
* User management
  * Custom user model
    * https://testdriven.io/blog/django-custom-user-model/
    * https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#referencing-the-user-model
    * https://learndjango.com/tutorials/django-best-practices-referencing-user-model
  * Full user authentication and authorization workflow (registration, login, email activation, password reset etc.)
  * Cookie sessions / Token sessions (TODO)
* S3 Bucket storage for files (TODO)
* Subscription to services (TODO)
  * Stripe integration

## Required enviromental variables

* `SECRET_KEY`
* `EMAIL_HOST`
* `EMAIL_USERNAME`
* `EMAIL_PASSWORD`
* `SECRET_KEY`
* `SECRET_KEY`


## Development

```bash
# Install requiremed packages
pip install -r requirements.txt

# Update for migrations and create local database
python manage.py makemigrations users
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

## Before Deployment

Read [official deployment checklist](https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/).

`settings.py`:
- [ ] Turn of Debugging
- [ ] Change Email Backend in 
- [ ] Secure cookies
- [ ] Secure `SECRET_KEY` 