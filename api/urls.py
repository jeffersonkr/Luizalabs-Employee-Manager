from django.urls import path
from api import views


urlpatterns = [
    path('', views.employees_list),
    path('<pk>', views.employee_details),
    path('register/', views.employee_register),
]