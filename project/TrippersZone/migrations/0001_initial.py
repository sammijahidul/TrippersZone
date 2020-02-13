# Generated by Django 2.2.7 on 2019-11-30 14:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Oid', models.CharField(max_length=225)),
                ('Oname', models.CharField(max_length=255)),
                ('Ocontact', models.CharField(max_length=255)),
                ('Olocation', models.CharField(max_length=255)),
                ('Ogender', models.CharField(max_length=255)),
                ('OnumOfRoom', models.CharField(max_length=255)),
                ('Ocapacity', models.CharField(max_length=255)),
                ('OroomRent', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OwnerPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Opost', models.CharField(max_length=300)),
                ('OpostedBy', models.CharField(max_length=225)),
                ('OpostTime', models.DateField(default=django.utils.timezone.now)),
                ('OnumOfRoom', models.CharField(max_length=10)),
                ('OroomRent', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='renter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rid', models.CharField(max_length=225)),
                ('Rname', models.CharField(max_length=255)),
                ('Rcontact', models.CharField(max_length=255)),
                ('Rlocation1', models.CharField(max_length=255)),
                ('Rlocation2', models.CharField(max_length=255)),
                ('Rgender', models.CharField(max_length=255)),
                ('RnumOfGuest', models.CharField(max_length=255)),
            ],
        ),
    ]
