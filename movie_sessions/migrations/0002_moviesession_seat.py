# Generated by Django 4.0.6 on 2022-07-18 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seats', '0001_initial'),
        ('movie_sessions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviesession',
            name='seat',
            field=models.ManyToManyField(related_name='movie_sessions', to='seats.seat'),
        ),
    ]