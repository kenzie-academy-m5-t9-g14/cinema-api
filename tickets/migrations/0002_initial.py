# Generated by Django 4.0.6 on 2022-07-19 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment_types', '0001_initial'),
        ('seats', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie_sessions', '0001_initial'),
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tickets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticket',
            name='movie_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tickets', to='movie_sessions.moviesession'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tickets', to='payment_types.paymenttype'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='seats',
            field=models.ManyToManyField(related_name='tickets', to='seats.seat'),
        ),
    ]
