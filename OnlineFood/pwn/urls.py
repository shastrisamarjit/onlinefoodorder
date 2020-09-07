
from django.urls import path

from pwn import views

urlpatterns = [

    path('',views.showIndex,name='pwn_main'),
    path('pwn_login_check/',views.pwn_login_check,name='pwn_login_check'),
    path('welcome/',views.welcome,name='welcome'),
    path('state/',views.openState,name='state'),
    path('save_state/', views.save_state, name="save_state"),
    path('deletestate/', views.deletestate, name="deletestate"),
    path('updatestate/', views.updatestate, name="updatestate"),
    path('city/',views.openCity,name='city'),
    path('save_city/', views.save_city, name="save_city"),
    path('deletecity/', views.deletecity, name="deletecity"),
    path('updatecity/', views.updatecity, name="updatecity"),
    path('cuisine/',views.openCusine,name='cuisine'),
    path('save_cuisine/', views.save_cuisine, name="save_cuisine"),
    path('deletecuisine/', views.deletecuisine, name="deletecuisine"),
    path('updatecuisine/', views.updatecuisine, name="updatecuisine"),
    path('vendor/',views.openVendor,name='vendor'),
    path('resports/',views.openReporsts,name='reports'),
    path('logout/',views.pwn_login_check,name='logout'),
]
