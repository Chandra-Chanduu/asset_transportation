from django.db import models

ASSET_CHOICES = (
    ('LAPTOP', 'Laptop'),
    ('TRAVEL_BAG', 'Travel Bag'),
    ('PACKAGE', 'Package'),
)

SENSITIVITY_CHOICES = (
    ('HIGHLY', 'HIGHLY_SENSITIVE'),
    ('SENSITIVE', 'SENSITIVE'),
    ('NORMAL', 'NORMAL'),
)

STATUS=(
    ('PENDING','Pending'),
    ('EXPIRED','Expired'),

)


class AssetTransportationRequest(models.Model):
    requester = models.CharField(max_length=100)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    date = models.DateField()
    no_of_assets = models.IntegerField()
    asset_type = models.CharField(max_length=20, choices=ASSET_CHOICES)
    sensitivity = models.CharField(max_length=20, choices=SENSITIVITY_CHOICES)
    deliver_to=models.CharField(max_length=100)
    status=models.CharField(max_length=30,choices=STATUS)

class Ride(models.Model):
    rider = models.CharField(max_length=100)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    dates = models.DateField()
    travel_medium = models.CharField(max_length=20)
    max_assets = models.IntegerField()
