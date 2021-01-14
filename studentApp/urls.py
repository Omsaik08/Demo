from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.homepage),
    path('insert/',views.insert),
    path('showstudent/',views.show),
    path('update/',views.update),
    path('delete/',views.delete),
]
