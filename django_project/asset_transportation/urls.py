from django.urls import path
from . import views

urlpatterns = [
    path('create_request',views.create_request,name='create_request'),
    path('',views.home,name='home'),
    path('retrieve',views.retrieve,name='retrieve'),
    path('request_sucess',views.request_success,name='request_success'),
    path('share_ride',views.share_ride,name='share_ride'),
    path('ride_success',views.ride_success,name='ride_success'),
    path('select_ride',views.select_ride,name='select_ride'),
]
