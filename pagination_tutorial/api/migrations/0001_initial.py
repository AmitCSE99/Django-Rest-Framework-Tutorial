# Generated by Django 3.2.9 on 2021-12-08 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
