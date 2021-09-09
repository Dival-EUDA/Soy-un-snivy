from django.urls import path
from .views import *


urlpatterns = [
    path('', init, name='init'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]

