from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('basiccourse', views.basiccourse, name='basiccourse'),
    path('dataanalytics', views.dataanalytics, name='dataanalytics'),
    path('datascience', views.datascience, name='datascience'),
    path('contact', views.contact, name='contact'),
    path('courses', views.courses, name='courses'),

    
]
