### Deploying in Local

If you are facing trouble running the application in local, install the following dependencies -

* pip install whitenoise
* pip install dj_database_url

If there is an import error, that means you don't have the local settings

* Create **local_settings.py** in the same directory as **settings.py**
* Paste the following code

> ```python
> import os
> 
> BASE_DIR=os.path.dirname(os.path.dirname(__file__))
> 
> DATABASES = {
>     'default': {
>         'ENGINE': 'django.db.backends.sqlite3',
>         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
>     }
> }
> 
> DEBUG = True
> ```