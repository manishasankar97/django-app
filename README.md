# django-app
#ReadMe File for application\
Create a new Django project using :\
django-admin.py startproject  projectname\

<h3>DEVELOPMENT</h3>
<h5>1. Set up Django\</h5>
To create a Django app, we’ll need to install Django. That’s easy enough!\
First, though, consider creating a new virtual environment for your project so you can manage your dependencies separately.\
<h5>1.1 Install Django\</h5>
Now, we can install Django:
$ pip install django
Next, let’s start a new Django project:\
django-admin startproject dsite\
If we look at the directory now, we’ll see that Django created a new folder for us:\
dir\
dsite/
And if we look inside that folder, there’s everything we need to run a Django site:\
cd dsite/\
 dir\
manage.py*  dsite/\
Let’s make sure it works. Test run the Django server:\
$ python manage.py runserver\
Watching for file changes with StatReloader\
Performing system checks...\
System check identified no issues (0 silenced).\
You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.\
Run 'python manage.py migrate' to apply them.\
sep 21, 2020 - 16:09:28\
Django version 2.2.1, using settings 'mysite.settings'\
Starting development server at http://127.0.0.1:8000/\
Quit the server with CONTROL-C.\
Go to localhost:8000 and you should see the Django welcome screen\
<h5>1.2 Create API app\</h5>
We could build our application with the folder structure the way it is right now. However, best practice is to separate your Django project into separate apps when you build\ something new.
So, let’s create a new app for our API:\
$ python manage.py startapp myapi\
$ ls\
db.sqlite3  manage.py*  myapi/  mysite/\
1.4 Register the myapi app with the mysite project\
We need to tell Django to recognize this new app that we just created. The steps we do later won’t work if Django doesn’t know about myapi.\
So, we edit mysite/settings.py :\
INSTALLED_APPS = [\
    'myapi.apps.MyapiConfig',\
    ... # Leave all the other INSTALLED_APPS\
]\
1.5 Migrate the database!\
Whenever we create or make changes to a model, we need to tell Django to migrate those changes to the database. The Django ORM then writes all the SQL CREATE TABLE commands for us.\
So, let’s migrate those initial models:\
$ python manage.py migrate\
Operations to perform:\
  Apply all migrations: admin, auth, contenttypes, sessions\
Running migrations:\
  Applying contenttypes.0001_initial... OK\
  Applying auth.0001_initial... OK\
  Applying admin.0001_initial... OK\
  Applying admin.0002_logentry_remove_auto_add... OK\
  Applying admin.0003_logentry_add_action_flag_choices... OK\
  Applying contenttypes.0002_remove_content_type_name... OK\
  Applying auth.0002_alter_permission_name_max_length... OK\
  Applying auth.0003_alter_user_email_max_length... OK\
  Applying auth.0004_alter_user_username_opts... OK\
  Applying auth.0005_alter_user_last_login_null... OK\
  Applying auth.0006_require_contenttypes_0002... OK\
  Applying auth.0007_alter_validators_add_error_messages... OK\
  Applying auth.0008_alter_user_username_max_length... OK\
  Applying auth.0009_alter_user_last_name_max_length... OK\
  Applying auth.0010_alter_group_name_max_length... OK\
  Applying auth.0011_update_proxy_permissions... OK\
  Applying sessions.0001_initial... OK\
1.6 Create Super User\
