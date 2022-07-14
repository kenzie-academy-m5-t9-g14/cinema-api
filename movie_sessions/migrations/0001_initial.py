# Generated by Django 4.0.6 on 2022-07-14 05:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        ('seats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieSession',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('exhibit_type', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_sessions', to='movies.moviesmodel')),
                ('seat', models.ManyToManyField(related_name='movie_sessions', to='seats.seat')),
            ],
        ),
    ]
