# 📰newsline
Local deployment instructions
Creating database:
1. Open `SQL Shell (psql)` (or use your IDE's GUI)
2. Enter login and password. For example, postgres, pass28282
3. Directly creating a database
```
postgres=# CREATE DATABASE newsline;
```

In folder newsline\newsline, settings.py set database parameters
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': newsline - your name of database
        'USER': 'postgres', - your user in psql
        'PASSWORD': 'pass28282', - your password in psql
        'HOST': 'localhost',
        'PORT': '5432', - your port in psql
    }
}
```


In project's folder (for example `D:\newsline>`) create virtual environment 
via command line or analogs.
```
D:\newsline>python -m venv venv
```

Activate virtual environment
```
D:\newsline>venv\scripts\activate
```

Install side libraries and frameworks
```
(venv) D:\newsline>pip install -r requirements.txt
```

Starting development server at localhost:
```
(venv) D:\newsline>python manage.py runserver
```

Add news and use pagination.
Delete news can only superusers.
To set superuser use:
```
(venv) D:\newsline>python manage.py createsuperuser
```
and re-enter login and password to admin page:
http://127.0.0.1:8000/admin/