from django.urls import path
from . import views 

urlpatterns=[
    path('',views.login),
    path('register/',views.register),
    path('studentdetails/',views.studentdetails),
    path('studentmarks/',views.studentmarks,name="marks"),



]
