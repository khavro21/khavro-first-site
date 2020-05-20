# Generated by Django 2.2.4 on 2020-04-29 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tmy_app', '0002_auto_20200428_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('city_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='LisbonClass',
        ),
        migrations.DeleteModel(
            name='MadeiraClass',
        ),
        migrations.DeleteModel(
            name='MoscowClass',
        ),
        migrations.DeleteModel(
            name='NurembergClass',
        ),
    ]
