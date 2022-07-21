# Generated by Django 4.0.6 on 2022-07-21 01:02


from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedules', '0001_initial'),
        ('movie_theaters', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieSession',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('exhibit_type', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('status_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_sessions', to='movies.moviesmodel')),
                ('movie_theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_sessions', to='movie_theaters.movietheater')),
                ('schedule', models.ManyToManyField(related_name='sessions', to='schedules.schedule')),
            ],
        ),
    ]
