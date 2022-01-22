from django.urls import path
from .views import sendsmsview

urlpatterns = [
    path("", sendsmsview.as_view(),name="send")
]