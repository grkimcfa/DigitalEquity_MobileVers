# Generated by Django 3.1.7 on 2021-04-09 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0018_auto_20210409_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programs',
            name='Tax1040',
        ),
    ]
