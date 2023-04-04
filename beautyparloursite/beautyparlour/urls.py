from django.urls import path
from .import views

urlpatterns=[
    path('front_log',views.login),
    path('reg',views.register),
    path('home',views.home),
    path('registered',views.registered),
    path('login',views.user_login),
    path('',views.profile),
    path('logout',views.logout),
    path('user_profile',views.user_profile),
    path('change_username',views.change_username),
    path('change_password',views.change_password),
    path('booking_haircut',views.booking_haircut),
    path('booked_haircut',views.booked_haircut),
    path('clear_booking',views.clear_booking),
    path('show_booking_details',views.show_booking_details),
    path('admin_reg',views.admin_reg),
    path('admin_show_booking',views.admin_show_booking),
    path('sort_by_latest',views.latest),
    path('sort_by_older',views.older),
    path('filter_by_date',views.filter_by_date),
    path('clear_booking',views.clear_booking),
    path('change_admin_username',views.change_admin_username),
    path('change_admin_password',views.change_admin_password),
    path('upload_gallery',views.upload_gallery),
    path('upload_quotes',views.upload_quotes),
    path('clear_quotes',views.clear_quotes),


]
