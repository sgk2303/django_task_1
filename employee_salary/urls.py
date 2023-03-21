from django.urls import path

from .views import * 

urlpatterns = [
    path('',highest_paid_employee, name='highest_paid_employee')
]