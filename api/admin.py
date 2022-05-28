from django.contrib import admin
from .models import Hero, Post, Company, Fuelinfo, Station
# Register your models here.
admin.site.register(Hero)
admin.site.register(Post)
admin.site.register(Company)
admin.site.register(Fuelinfo)
admin.site.register(Station)