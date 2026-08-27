from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tickets, name='ticket_list'),
    path('toggle/<int:pk>/', views.toggle_status, name='toggle_status'),
]
