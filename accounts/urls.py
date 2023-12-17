from . import views
from django.urls import path

urlpatterns = [    
	path("login/", views.login, name="login"),
    path("signup/customer/", views.new_customer, name="new_customer"),
    path("signup/driver/", views.new_driver, name="new_driver"),
    path("logout/", views.logout, name="logout"),
    
]

