from django.urls import path
from . import views

urlpatterns = [
    path('country_info/<str:country_name>', views.country_info, name='country_info'),
    
]
