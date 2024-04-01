from django.urls import path
from .views import CommandList, CommandDetail

urlpatterns = [
    path('commands/', CommandList.as_view(), name='command_list'),
    path('commands/<int:pk>', CommandDetail.as_view(), name='command_detail'),
]
