# django-app
#ReadMe File for application
Create a new Django project using :
django-admin.py startproject  projectname
##DEVELOPMENT
#1. Set up Django
To create a Django app, we’ll need to install Django. That’s easy enough!
First, though, consider creating a new virtual environment for your project so you can manage your dependencies separately.
#1.2 Install Django
Now, we can install Django:
$ pip install django
Next, let’s start a new Django project:
>> django-admin startproject dsite
If we look at the directory now, we’ll see that Django created a new folder for us:
>> dir
dsite/
And if we look inside that folder, there’s everything we need to run a Django site:
>>cd dsite/
>> dir
manage.py*  dsite/
Let’s make sure it works. Test run the Django server:
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).
You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
sep 21, 2020 - 16:09:28
Django version 2.2.1, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Go to localhost:8000 and you should see the Django welcome screen!

