from rest_framework import serializers
from .models import User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','real_name','tz','start_time','end_time')