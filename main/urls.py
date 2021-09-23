from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('index.html',views.index,name='home'),
    path('contact.html',views.contact,name='contact'),
    path('about.html',views.about,name='about'),
    path('gallery.html',views.gallery,name='gallery'),

    
]