from django.urls import path
from .views import home, subscribe
urlpatterns = [
    path('', home, name='home'),
    path('clicked/', subscribe, name='subscribe'),
]