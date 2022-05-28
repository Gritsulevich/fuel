from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name
        
class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    slug = models.SlugField(verbose_name='URL', max_length=150, unique=True, db_index = True)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    

    class Meta:
        ordering = ['created']
    def __str__(self):
        return self.title

class Company(models.Model):
    owner = models.CharField(max_length=28, blank=True, default='')
    title = models.CharField(max_length=50, blank=True, default='')
    logo = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    
class Fuelinfo(models.Model):
    FUEL_TYPE = [
        ('D', 'Diesel'),
        ('D', 'Gasoline'),
        ('G', 'Gas'),]
    
    title = title = models.CharField(max_length=50, blank=True, default='')
    fuel_type = models.CharField(
        max_length=15,
        choices=FUEL_TYPE,
        default="None",)
        
    quantity_limit = models.BigIntegerField(verbose_name='How many liters?')
    avallabilly = models.BooleanField()
    timestamp_create = models.DateField(auto_now=True)
    timestamp_update = models.DateField(auto_now_add=True)
    staItionId = models.ForeignKey("Station", related_name='Station', on_delete=models.CASCADE)
    
class Station(models.Model):
    json_work = [
        {
        "day":1,
        "start": "10:00",
        "end":"18:00"
        },
        ]
    company_id = models.ForeignKey('Company', related_name='Company', on_delete=models.CASCADE)
    latitude = models.BigIntegerField()
    lingitude = models.BigIntegerField()
    adress = models.CharField(max_length=50, blank=True, default='')
    additionalinfo = models.TextField(blank=True, default='')
    work_schedule = models.JSONField()
    currency_type = models.CharField(max_length=3, blank=False, default='UAH')
    timestamp_create = models.DateField(auto_now=True)
    timestamp_update = models.DateField(auto_now_add=True)
    