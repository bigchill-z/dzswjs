from django.urls import path
from .views import *

urlpatterns = [
    path('ranks', DouyinAPIView.as_view(), name='douyin'),
]