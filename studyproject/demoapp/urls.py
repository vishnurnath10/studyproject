from .import views
from django.urls import path

urlpatterns = [

   # path('',views.start,name='start'),
   #  path('about/',views.about,name='about'),
   #  path('contact/', views.contact, name='contact'),
   #  path('ad/',views.addition,name='addition'),
    path('',views.develop,name='develop')


]
