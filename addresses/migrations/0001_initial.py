# Generated by Django 4.0.6 on 2022-07-13 20:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=8)),
            ],
        ),
    ]
