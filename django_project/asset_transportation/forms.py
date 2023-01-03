from django import forms
from .models import AssetTransportationRequest, Ride
from django.forms.widgets import DateTimeInput



class AssetTransportationRequestForm(forms.Form):
    requester = forms.CharField(max_length=100)
    start_location = forms.CharField(max_length=100)
    end_location = forms.CharField(max_length=100)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    no_of_assets = forms.IntegerField()
    asset_type = forms.ChoiceField(choices=[
        ('LAPTOP', 'Laptop'),
        ('TRAVEL_BAG', 'Travel Bag'),
        ('PACKAGE', 'Package'),
    ])
    sensitivity = forms.ChoiceField(choices=[
        ('HIGHLY', 'HIGHLY_SENSITIVE'),
        ('SENSITIVE', 'SENSITIVE'),
        ('NORMAL', 'NORMAL'),
    ])
    deliver_to=forms.CharField(max_length=100)
    status=(
    ('PENDING','Pending'),
    ('EXPIRED','Expired'),

)

class RideForm(forms.Form):
    rider = forms.CharField(max_length=100)
    start_location = forms.CharField(max_length=100)
    end_location = forms.CharField(max_length=100)
    dates = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    travel_medium = forms.ChoiceField(choices=[
        ('CAR', 'Car'),
        ('BUS', 'Bus'),
        ('TRAIN', 'Train'),
    ])
    max_assets = forms.IntegerField()

