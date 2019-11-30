from django.urls import path

from summergeeks.views import create_host, create_visitor, checkout_visitor


urlpatterns = [
    path('create_host', create_host, name='create_host'),
    path('create_visitor', create_visitor, name='create_visitor'),
    path('checkout_visitor', checkout_visitor, name='checkout_visitor'),
]
