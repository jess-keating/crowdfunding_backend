from django.urls import path
from . import views

urlpatterns = [
    path('', views.FundraiserList.as_view(), name='fundraiser-list'),
]