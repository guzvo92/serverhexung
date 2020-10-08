Download (db browser for sqlite)
Abrir path y arrastrar archivo
equivalente al navycat (gestor visual)
-----------------------------------------------------------
django-admin startproject pyserver . (genera el manage.py)

python manage.py sqlmigrate myapp 0001
python manage.py makemigrations
python manage.py migrate (genera db)
python manage.py runserver (load local)

python manage.py help
-------------------------------------------------------
python manage.py startapp myapp
---------------------------------------------------------
agregar en configs.py
MEDIA_URL='/media/'
STATICFILES_DIRS=[BASE_DIR +"/assets",]
STATIC_ROOT='/home/***username***/public_html/static'
MEDIA_ROOT='/home/*** user name***/public_html/media'
-----------------------------------------------------------

admin
python manage.py createsuperuser
