# Generated by Django 4.0.4 on 2022-05-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_company_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='owner',
            field=models.CharField(blank=True, default='', max_length=28),
        ),
    ]