# Generated by Django 3.2.4 on 2022-07-25 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thanks',
            fields=[
                ('thanks_id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('thanks_title', models.CharField(max_length=100)),
                ('thanks_date', models.DateTimeField()),
                ('thanks_description', models.CharField(max_length=1000)),
                ('givethanks_count', models.IntegerField()),
            ],
        ),
    ]
