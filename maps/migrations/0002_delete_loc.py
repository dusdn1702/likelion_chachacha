# Generated by Django 2.2.4 on 2019-08-08 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_heart'),
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Loc',
        ),
    ]
