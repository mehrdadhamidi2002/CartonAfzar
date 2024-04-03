from django.urls import path, include
from .views import home, subscribe,create_contact
urlpatterns = [
    path('', home, name='home'),
    path('clicked/', subscribe, name='subscribe'),
    path('contact/', create_contact, name='create_contact'),
]