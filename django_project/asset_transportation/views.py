import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .forms import AssetTransportationRequestForm, RideForm
from .models import AssetTransportationRequest, Ride
from django.urls import reverse
from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import AssetTransportationRequest

request_id=-1
cursor=connection.cursor()
#Cursor connection

def home(request):
    if request.method == 'POST':
        button = request.POST.get('button')
        if button !=None:
            if button == 'request':
                return redirect('create_request')
            elif button == 'ride':
                return redirect('share_ride')
            elif button == 'asset_request':
                return redirect('retrieve')
        else:
            return render(request,'home.html')
    else:
        return render(request,'home.html')

def update_request_status(request):
    requests = AssetTransportationRequest.objects.filter(date__lt=datetime.datetime.now())
    requests.update(status="EXPIRED")




def retrieve(request):
    global request_id
    update_request_status(request)
    rows=AssetTransportationRequest.objects.order_by('-date')
    return render(request, 'asset_requests.html', {'requests': rows})



def create_request(request):
    update_request_status(request)
    if request.method == 'POST':
        form = AssetTransportationRequestForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            asset_transportation_request = AssetTransportationRequest(
            start_location=data['start_location'],
            end_location=data['end_location'],
            asset_type=data['asset_type'],
            sensitivity=data['sensitivity'],
            date=data['date'],
            no_of_assets=data['no_of_assets'],
            deliver_to=data['deliver_to'],
            status='PENDING'
            )
            asset_transportation_request.save()
            global request_id
            request_id=AssetTransportationRequest.objects.last().id
            return redirect('select_ride')
    else:
        form = AssetTransportationRequestForm()
    return render(request, 'create_request.html', {'form': form})




def select_ride(request):
    requests = Ride.objects.all()
    if request.method == 'POST':
        global request_id
        ride_id=request.POST.get('get_ride_id')
        cursor.execute('select max_assets from asset_transportation_ride where id='+str(ride_id)+';')
        max_assets=cursor.fetchone()
        cursor.execute('select no_of_assets from asset_transportation_assettransportationrequest where id='+str(request_id)+';')
        no_of_assets=cursor.fetchone()
        k=max_assets[0]-no_of_assets[0]
        if k<0:
            return render(request, 'rides.html', {'rides': requests})
        else:
            cursor.execute('update asset_transportation_ride set max_assets='+str(k)+' where id='+str(ride_id)+';')
            return redirect('retrieve')
    return render(request, 'rides.html', {'rides': requests})

def request_success(request):
    requests = AssetTransportationRequest.objects.all()
    return render(request, 'requests.html', {'requests': requests})

def share_ride(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            share_ride_request=Ride(
                rider=data['rider'],
                start_location=data['start_location'],
                end_location=data['end_location'],
                dates=data['dates'],
                travel_medium=data['travel_medium'],
                max_assets=data['max_assets'],
            )
            share_ride_request.save()
            return render(request, 'ride_info.html')
    else:
        form = RideForm()
    return render(request, 'share_ride.html', {'form': form})

def ride_success(request):
    requests = Ride.objects.all()
    return render(request, 'rides.html', {'rides': requests})

