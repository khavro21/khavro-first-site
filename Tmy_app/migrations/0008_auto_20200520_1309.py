# Generated by Django 2.2.4 on 2020-05-20 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tmy_app', '0007_auto_20200519_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_info',
            field=models.TextField(blank=True),
        ),
    ]