<h6>django-app</h6>
#ReadMe File for application<br/>
Create a new Django project using :<br/>
django-admin.py startproject  projectname<br/>

<h3>DEVELOPMENT</h3>
<h4>1. Set up Django</h4>
To create a Django app, we’ll need to install Django. That’s easy enough!\<br />
First, though, consider creating a new virtual environment for your project so you can manage your dependencies separately.<br />
<h4>1.1 Install Django</h4>
Now, we can install Django:<br />
$ pip install django<br />
Next, let’s start a new Django project:<br />
django-admin startproject dsite<br />
If we look at the directory now, we’ll see that Django created a new folder for us:<br />
dir/<br />
dsite/<br />
And if we look inside that folder, there’s everything we need to run a Django site:<br />
cd dsite/<br />
 dir<br />
manage.py*  dsite/<br />
Let’s make sure it works. Test run the Django server:<br />
$ python manage.py runserver<br />
Watching for file changes with StatReloader<br />
Performing system checks...<br />
System check identified no issues (0 silenced).<br />
You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.<br />
Run 'python manage.py migrate' to apply them.<br />
sep 21, 2020 - 16:09:28<br />
Django version 2.2.1, using settings 'mysite.settings'<br />
Starting development server at http://127.0.0.1:8000/<br />
Quit the server with CONTROL-C.<br />
Go to localhost:8000 and you should see the Django welcome screen<br />

<h4>1.2 Create API app\</h4>
We could build our application with the folder structure the way it is right now. However, best practice is to separate your Django project into separate apps when you build something new.<br />
So, let’s create a new app for our API:<br />
$ python manage.py startapp myapi<br />
$ ls\<br />
db.sqlite3  manage.py*  myapi/  mysite/<br />
<h4>1.3 Register the myapi app with the mysite project</h4><br />
We need to tell Django to recognize this new app that we just created. The steps we do later won’t work if Django doesn’t know about myapi.<br />
So, we edit mysite/settings.py :<br />
INSTALLED_APPS = [<br />
    'myapi.apps.MyapiConfig',<br />
    ... # Leave all the other INSTALLED_APPS<br />
]<br />
<h4>1.4Migrate the database!</h4><br />
Whenever we create or make changes to a model, we need to tell Django to migrate those changes to the database. The Django ORM then writes all the SQL CREATE TABLE commands for us.<br />
So, let’s migrate those initial models:<br />
$ python manage.py migrate<br />
Operations to perform:<br />
  Apply all migrations: admin, auth, contenttypes, sessions<br />
Running migrations:<br />
  Applying contenttypes.0001_initial... OK\<br />
  Applying auth.0001_initial... OK\<br />
  Applying admin.0001_initial... OK\<br />
  Applying admin.0002_logentry_remove_auto_add... OK\<br />
  Applying admin.0003_logentry_add_action_flag_choices... OK\<br />
  Applying contenttypes.0002_remove_content_type_name... OK\<br />
  Applying auth.0002_alter_permission_name_max_length... OK\<br />
  Applying auth.0003_alter_user_email_max_length... OK\<br />
  Applying auth.0004_alter_user_username_opts... OK\<br />
  Applying auth.0005_alter_user_last_login_null... OK\<br />
  Applying auth.0006_require_contenttypes_0002... OK\<br />
  Applying auth.0007_alter_validators_add_error_messages... OK\<br />
  Applying auth.0008_alter_user_username_max_length... OK\<br />
  Applying auth.0009_alter_user_last_name_max_length... OK\<br />
  Applying auth.0010_alter_group_name_max_length... OK\<br />
  Applying auth.0011_update_proxy_permissions... OK\<br />
  Applying sessions.0001_initial... OK\<br />
<h4>1.5 Create Super User</h4><br />
It would be nice if we had access to Django’s pretty admin interface when we want to review the data in our database.<br/>
To do so, we’ll need login credentials. So, let’s make ourselves the owners and administrators of this project. THE ALL-POWERFUL SUPERUSER!!!<br/>
$ python manage.py createsuperuser<br/>
Username (leave blank to use 'manisha'): <br/>
Email address: manisha@admin.com<br />
Password: <br />
Password (again): <br />
Superuser created successfully.<br />
Let’s verify that it works. Start up the Django server:<br />
$ python manage.py runserver<br />
And then navigate to localhost:8000/admin<br />

Oooo, Django Admin!!! Pretty.<br />
Log in with your superuser credentials, and you should see the admin dashboard:<br />

Look at those lovely User and Group models<br />
<h4>2. Create a model in the database that Django ORM will manage</h4><br />
Let’s make our first model!<br />
We’ll build it in myapi/models.py , so open up that file.<br />
<h4>2.1 myapi/models.py</h4><br />
Let’s make a database of superheroes! Each hero has a name and an alias that they go by in normal life. We’ll start there with our model:<br />
# models.py<br />
from django.db import models<br />
class User(models.Model):<br />
    real_name = models.CharField(max_length=60)<br />
    tz = models.CharField(max_length=60)<br />
    start_time = datetime.datetime.now()<br />
    end_time = datetime.datetime.now()<br />
    activity_period = {'start_time' : start_time,'end_time': end_time}<br />
    def __str__(self):<br />
        return self.real_name<br />
        return self.tz<br />
        return self.activity_period<br />
 real_name,tz,start_time etc., are character fields where we can store strings. The __str__ method just tells Django what to print when it needs to print out an instance of the User model.<br />
<h4>2.2 Make migrations</h4><br />
Remember, whenever we define or change a model, we need to tell Django to migrate those changes.<br />
$ python manage.py makemigrations
Migrations for 'dapi':<br />
  dapi/migrations/0001_initial.py<br />
    - Create model User<br />
$ python manage.py migrate<br />
Operations to perform:<br />
  Apply all migrations: admin, auth, contenttypes, myapi, sessions<br />
Running migrations:<br />
  Applying dapi.0001_initial... OK<br />
<h4>2.3 Register User with the admin site</h4><br />
Remember that awesome admin site that comes out of the box with Django?<br />
It doesn’t know the Hero model exists, but with two lines of code, we can tell it about User.<br />
Open dapi/admin.py and make it look like this:<br />
from django.contrib import admin<br />
from .models import User<br />
admin.site.register(User)<br />
Now run the Django server:<br />
$ python manage.py runserver<br />
And visit localhost:8000/admin<br />

<h4>2.4 Create some new heroes</h4><br />
While we’re on the admin site, might as well create a few heroes to play around with in our application.<br />
Click “Add.” Then, make your users!<br />
<h4>3. Set up Django REST Framework</h4><br />
Okay, time to start thinking about our Users API. We need to serialize the data from our database via endpoints.<br />
To do that, we’ll need Django REST Framework, so let’s get that installed.<br />
$ pip install djangorestframework<br />
Now, tell Django that we installed the REST Framework in dsite/settings.py:<br />
INSTALLED_APPS = [<br />
    # All your installed apps stay the same<br />
    ...<br />
    'rest_framework',<br />
]<br />
That’s it!<br />
<h4>4. Serialize the User model</h4><br />
Now we’re starting to get into some new waters. We need to tell REST Framework about our Hero model and how it should serialize the data.
Remember, serialization is the process of converting a Model to JSON. Using a serializer, we can specify what fields should be present in the JSON representation of the model.
The serializer will turn our heroes into a JSON representation so the API user can parse them, even if they’re not using Python. In turn, when a user POSTs JSON data to our API, the serializer will convert that JSON to a Hero model for us to save or validate.<br />
To do so, let’s create a new file — dapi/serializers.py<br />
In this file, we need to:<br />
Import the User model<br />
Import the REST Framework serializer<br />
Create a new class that links the User with its serializer<br />
Here’s how:<br />
# serializers.py<br />
from rest_framework import serializers<br />

from .models import User<br />

class UserSerializer(serializers.HyperlinkedModelSerializer):<br />
    class Meta:<br />
        model = User<br />
        fields = ('real_name', 'tz')<br />
<h4>5. Display the data</h4><br />
Now, all that’s left to do is wire up the URLs and views to display the data!<br />
<h4>5.1 Views</h4><br />
Let’s start with the view. We need to render the different Users in JSON format.<br />
To do so, we need to:<br />
Query the database for all Users<br />
Pass that database queryset into the serializer we just created, so that it gets converted into JSON and rendered<br />
In dapi/views.py:<br />
# views.py<br />
from rest_framework import viewsets<br />

from .serializers import UserSerializer<br />
from .models import User<br />


class UserViewSet(viewsets.ModelViewSet):<br />
    queryset = User.objects.all().order_by('name')<br />
    serializer_class = UserSerializer<br />
ModelViewSet is a special view that Django Rest Framework provides. It will handle GET and POST for Heroes without us having to do any more work.<br />
<h4>5.2 Site URLs</h4><br />
Okay, awesome. We’re soooooo close. The last step is to point a URL at the viewset we just created.<br />
In Django, URLs get resolved at the project level first. So there’s a file in mysite/ directory called urls.py .<br />
Head over there. You’ll see the URL for the admin site is already in there. Now, we just need to add a URL for our API. For now, let’s just put our API at the index:<br />
# dsite/urls.py<br />
from django.contrib import admin<br />
from django.urls import path, include<br />

urlpatterns = [<br />
    path('admin/', admin.site.urls),<br />
    path('', include('dapi.urls')),<br />
 ]
<h4>5.3 API URLs</h4><br />
If you’re paying attention and not just blindly copy-pasting, you’ll notice that we included 'dapi.urls' . That’s a path to a file we haven’t edited yet. And that’s where Django is going to look next for instructions on how to route this URL.<br />
So, let’s go there next — dapi/urls.py:<br />
# dapi/urls.py<br />
from django.urls import include, path<br />
from rest_framework import routers<br />
from . import views<br />

router = routers.DefaultRouter()<br />
router.register(r'Users', views.UserViewSet)<br />

# Wire up our API using automatic URL routing.<br />
# Additionally, we include login URLs for the browsable API.<br />
urlpatterns = [<br />
    path('', include(router.urls)),<br />
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))<br />
]
Notice we added something called router that we imported from rest_framework.<br />
The REST Framework router will make sure our requests end up at the right resource dynamically. If we add or delete items from the database, the URLs will update to match. Cool right?<br />
A router works with a viewset (see views.py above) to dynamically route requests. In order for a router to work, it needs to point to a viewset, and in most cases, if you have a viewset you’ll want a router to go with it.<br />
So far, we’ve only added one model+serializer+viewset to the router — Heroes. But we can add more in the future repeating the same process above for different models! (Maybe create a Villains API next?)<br />
Of course, if you only want to use standard DRF Views instead of viewsets, then urls.py will look a little different. You don’t need a router to use simple views, and you can <br />just add them with:<br />
path('path/to/my/view/', MySimpleView.as_view())<br />
Test it out!<br />
Start up the Django server again:<br />
$ python manage.py runserver<br />
Now go to localhost:8000<br />
Image for post<br />
The root of our new API — Django REST Framework makes it look nice<br />
Visit the endpoint via GET<br />
If we click the link (Hyperlinks are good REST-ful design, btw), we see the heroes API results:<br />
Image for post<br />
GET an Individual Hero<br />
We can GET a single model instance using its ID.<br />
Django REST Framework viewsets take care of this for us.<br />
If you go to 127.0.0.1:8000/users/<id>/ where <id> is the ID of one of your Heroes models, you’ll be able to see just that user.<br />
For example, http://127.0.0.1:8000/heroes/1/ for me returns:<br />

}
We can make this a little more user-friendly by adding ID into the users/ endpoint response. In dapi/serializers.py, change the fields list to include “id”:<br />
class UserSerializer(serializers.HyperlinkedModelSerializer):<br />
    class Meta:<br />
        model = User<br />
        fields = (‘id’, ‘name’, ‘alias’)<br />
Now the hero list looks like this:<br />
GET /heroes/<br />
HTTP 200 OK<br />
Allow: GET, POST, HEAD, OPTIONS<br />
Content-Type: application/json<br />
Vary: Accept<br />
[<br />
    {<br />
        "id": 3,<br />
        "real_name": "Egon Spengler",<br />
        "tz": "America/Los_Angeles",<br />
        "activity_period": {<br />
            "start_time": "2020-09-23T12:05:55.841179",<br />
            "end_time": "2020-09-23T12:05:55.841179"<br />
        }<br />
    },<br />
We can use those IDs to look up individual models.<br />
Send a POST request<br />
Our API also handles post requests. We can send JSON to the API and it will create a new record in the database.<br />

Sending a POST request to our API<br />
