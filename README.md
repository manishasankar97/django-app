<h1>README FILE for django-app</h1>

Create a new Django project using :<br />
  $django-admin.py startproject  projectname<br/>
<h3>1. Set up Django:</h3>
To create a Django app, we’ll need to install Django. <br />
  <h4>1.1 Install Django</h4>\
    $ pip install django <br /> 
Next, let’s start a new Django project:<br />
  $django-admin startproject dsite <br />
  
Now, we’ll see that Django created a new folder for us:<br />
  dir/  <br/>
  dsite <br />

And if we look inside that folder, there’s everything we need to run a Django site:<br />
  cd dsite/<br/>
   dir\<br/>
  manage.py*  dsite/<br />

To make sure it works. Test run the Django server:<br />
            $ python manage.py runserver <br/>
            Watching for file changes with StatReloader<br/>
            Performing system checks...<br/>
            System check identified no issues (0 silenced).<br/>
            You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions. <br/> 
            Run 'python manage.py migrate' to apply them.  <br/>
            sep 21, 2020 - 16:09:28  <br/>
            Django version 3.1.1, using settings 'dsite.settings' <br/> 
            Starting development server at http://127.0.0.1:8000/ <br/> 
            Quit the server with CONTROL-C. <br />
Go to localhost:8000 and you should see the Django welcome screen<br />

<h4>1.2 Create API app\</h4>
 To separate your Django project into separate apps when you build something new.<br />
    Let’s create a new app for our API:<br />
   $ python manage.py startapp dapi<br />
   $ ls\<br />
   db.sqlite3  manage.py*  dapi/  dsite/<br />
   
<h4>1.3 Register the dapi app with the dsite project\</h4>
We need to tell Django to recognize this new app that we just created.<br />
So, we edit dsite/settings.py :<br />
     INSTALLED_APPS = [<br />
        'dapi.apps.dapiConfig',<br />
        ... # Leave all the other INSTALLED_APPS<br />
      ]<br />

<h4>1.4Migrate the database!\</h4>
Whenever we create or make changes to a model, we need to tell Django to migrate those changes to the database. The Django ORM then writes all the SQL CREATE TABLE commands for us.<br />
So, let’s migrate those initial models:<br />
         $ python manage.py migrate
            Operations to perform:
              Apply all migrations: admin, auth, contenttypes, sessions
            Running migrations:
               Applying contenttypes.0001_initial... OK<br/>
               Applying auth.0001_initial... OK<br/>
               Applying admin.0001_initial... OK<br/>
               Applying admin.0002_logentry_remove_auto_add... OK<br/>
               Applying admin.0003_logentry_add_action_flag_choices... OK<br/>
               Applying contenttypes.0002_remove_content_type_name... OK<br/>
               Applying auth.0002_alter_permission_name_max_length... OK<br/>
               Applying auth.0003_alter_user_email_max_length... OK<br/>
               Applying auth.0004_alter_user_username_opts... OK<br/>
               Applying auth.0005_alter_user_last_login_null... OK<br/>
               Applying auth.0006_require_contenttypes_0002... OK<br/>
               Applying auth.0007_alter_validators_add_error_messages... OK<br/>
               Applying auth.0008_alter_user_username_max_length... OK<br/>
               Applying auth.0009_alter_user_last_name_max_length... OK<br/>
               Applying auth.0010_alter_group_name_max_length... OK<br/>
               Applying auth.0011_update_proxy_permissions... OK<br/>
               Applying sessions.0001_initial... OK <br/>
       
       
<h4>1.5 Create Super User\</h4>
It would be nice if we had access to Django’s pretty admin interface when we want to review the data in our database.<br/>
To do so, we’ll need login credentials. So, let’s make ourselves the owners and administrators of this project.<br/>
            $ python manage.py createsuperuser<br/>
             Username (leave blank to use 'manisha'): <br/>
             Email address: manisha@admin.com<br />
             Password: <br />
             Password (again): <br />
             Superuser created successfully.<br />
Let’s verify that it works. Start up the Django server:<br />
       $ python manage.py runserver<br />
 And then navigate to localhost:8000/admin<br />
Log in with your superuser credentials, and you should see the admin dashboard:<br />

<h3>2. Create a model in the database that Django ORM will manage\</h3>
Let’s make our first model!<br />
We’ll build it in dapi/models.py , so open up that file.<br />


<h4>2.1 dapi/models.py\</h4>
Let’s make a database of superusers! Each user has a name and an tz. We’ll start there with our model:<br />
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
 
 
<h4>2.2 Make migrations\</h4>
Whenever we define or change a model, we need to tell Django to migrate those changes.<br />
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
Remember that admin site that comes out of the box with Django?<br />
It doesn’t know the User model exists, but with two lines of code, we can tell it about User.<br />
   Open dapi/admin.py :<br />
    from django.contrib import admin<br />
    from .models import User<br />
    admin.site.register(User)<br /> 

Now run the Django server:<br />
  $ python manage.py runserver<br />
And visit localhost:8000/admin<br />

<h4>2.4 Create some new users</h4><br />
While we’re on the admin site, might as well create a few users in our application.<br />
Click “Add.” Then, add users!<br />

<h4>3. Set up Django REST Framework</h4><br />
 We need to serialize the data from our database via endpoints.<br />
 To do that, we’ll need Django REST Framework, so let’s get that installed.<br />
  `$ pip install djangorestframework<br />`
 Now, tell Django that we installed the REST Framework in dsite/settings.py:<br />
  `INSTALLED_APPS = [<br />
      # All your installed apps stay the same<br />
      ...<br />
      'rest_framework',<br />
  ]<br />`
  
<h4>4. Serialize the User model</h4><br />
 We need to tell REST Framework about our User model and how it should serialize the data.
 Serialization is the process of converting a Model to JSON. Using a serializer, we can specify what fields should be present in the JSON representation of the model.
 To do so, let’s create a new file — dapi/serializers.py<br />
 In this file, we need to:<br />
 1.Import the User model<br />
 2.Import the REST Framework serializer<br /> 
 
 Create a new class that links the User with its serializer<br />
Here’s how:<br />
     # serializers.py<br />
      from rest_framework import serializers<br />
      from .models import User<br />
      class UserSerializer(serializers.HyperlinkedModelSerializer):<br />
          class Meta:<br />
              model = User<br />
              fields = ('real_name', 'tz','activity_period')<br />

        
<h4>5. Display the data</h4><br />
Now,to wire up the URLs and views to display the data!<br />

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

ModelViewSet is a special view that Django Rest Framework provides. It will handle GET and POST for User .<br />


<h4>5.2 Site URLs</h4><br />
 The last step is to point a URL at the viewset we just created.<br />
In Django, URLs get resolved at the project level first. So there’s a file in dsite/ directory called urls.py .<br />
You’ll see the URL for the admin site is already in there. Now, we just need to add a URL for our API. For now, let’s just put our API at the index:<br />
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
       router = routers.DefaultRouter()
       router.register(r'Users', views.UserViewSet)<br />
       # Wire up our API using automatic URL routing.<br />
       # Additionally, we include login URLs for the browsable API.<br />
       urlpatterns = [<br />
           path('', include(router.urls)),<br />
           path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))<br />
       ]
Notice we added something called router that we imported from rest_framework.<br />
The REST Framework router will make sure our requests end up at the right resource dynamically. If we add or delete items from the database, the URLs will update to match. <br />
A router works with a viewset (see views.py above) to dynamically route requests. In order for a router to work, it needs to point to a viewset, and in most cases, if you have a viewset you’ll want a router to go with it.<br /> 
Test it out!<br />


Start up the Django server again:<br />
  $ python manage.py runserver<br />
Now go to localhost:8000<br />

The root of our new API — Django REST Framework makes it look nice<br />
Visit the endpoint via GET<br />
If we click the link , we see the users API results:<br />

GET an Individual User<br />
We can GET a single model instance using its ID.<br />
Django REST Framework viewsets take care of this for us.<br />
If you go to 127.0.0.1:8000/users/<id>/ where <id> is the ID of one of your User models, you’ll be able to see just that user.<br />
For example,"users": "http://127.0.0.1:8000/users/" for me returns:<br />
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
