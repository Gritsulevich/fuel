from rest_framework import serializers

from .models import Hero, Post, Company, Fuelinfo, Station

from django.contrib.auth.models import User

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Company
        fields = ('id','owner','title', 'logo', 'description')


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'slug', 'owner']


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']
 
class FuelinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuelinfo
        fields = ['id', 'title', 'fuel_type', "quantity_limit", 'avallabilly','timestamp_create', 'timestamp_update', 'staItionId']

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'company_id', 'latitude', "lingitude", 'adress','additionalinfo', 'work_schedule', 'currency_type', 'timestamp_create', 'timestamp_update']