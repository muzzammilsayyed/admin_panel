# partners/urls.py
from django.urls import path
from .views import dashboard, partner_list
from . import views


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('partners/', partner_list, name='partner_list'),
    path('add/', views.add_partner, name='add_partner'),
    path('details/<int:pk>/', views.partner_details, name='partner_details'),
    path('edit/<int:pk>/', views.edit_partner, name='edit_partner'),
    
    # other paths...
]


