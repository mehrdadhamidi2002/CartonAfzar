from django.urls import path, include
from .views import home, subscribe,create_contact, sitemessages_grid_view, filter_messages, print_invoice

app_name = 'tss'

urlpatterns = [
    path('', home, name='home'),
    path('clicked/', subscribe, name='subscribe'),
    path('contact/', create_contact, name='create_contact'),
    path('sitemessages/', sitemessages_grid_view, name='sitemessages_grid_view'),
    path('filter_messages/', filter_messages, name='filter_messages'),
    path('print_invoice/', print_invoice, name='print_invoice'),
]