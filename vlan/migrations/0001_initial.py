# Generated by Django 2.2.4 on 2019-08-08 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onuid', models.CharField(max_length=255)),
                ('onumac', models.CharField(max_length=255)),
                ('onuaddress', models.CharField(max_length=255)),
                ('onuvlan', models.CharField(max_length=4)),
                ('eocmac', models.CharField(max_length=255)),
                ('eocip', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('author', models.CharField(max_length=255)),
            ],
        ),
    ]
