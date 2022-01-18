from unicodedata import name
from django.urls import path
from sms.views import contact

app_name = 'sms'
urlpatterns = [
    path('form/', contact, name = 'contact')
]