from django.db import models
import datetime

class User(models.Model):
    real_name = models.CharField(max_length=60)
    tz = models.CharField(max_length=60)
    start_time = datetime.datetime.now()
    end_time = datetime.datetime.now()
    activity_period = {'start_time' : start_time,'end_time': end_time}
    def __str__(self):
        return self.real_name
        return self.tz
        return self.activity_period
