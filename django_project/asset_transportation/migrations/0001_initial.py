# Generated by Django 4.1.4 on 2023-01-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetTransportationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester', models.CharField(max_length=100)),
                ('start_location', models.CharField(max_length=100)),
                ('end_location', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('no_of_assets', models.IntegerField()),
                ('asset_type', models.CharField(choices=[('LAPTOP', 'Laptop'), ('TRAVEL_BAG', 'Travel Bag'), ('PACKAGE', 'Package')], max_length=20)),
                ('sensitivity', models.CharField(choices=[('HIGHLY', 'HIGHLY_SENSITIVE'), ('SENSITIVE', 'SENSITIVE'), ('NORMAL', 'NORMAL')], max_length=20)),
                ('deliver_to', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('EXPIRED', 'Expired')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rider', models.CharField(max_length=100)),
                ('start_location', models.CharField(max_length=100)),
                ('end_location', models.CharField(max_length=100)),
                ('dates', models.DateField()),
                ('travel_medium', models.CharField(max_length=20)),
                ('max_assets', models.IntegerField()),
            ],
        ),
    ]
