from django.contrib import admin
from django.urls import path
from trucks.views import login_view, logout_view, register_view, weighbridge_ticket_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('weighbridge-ticket/<str:vehicle_number>/', weighbridge_ticket_view, name='weighbridge_ticket'),
    path('', home_view, name='home'),
    path('ticket/', weighbridge_ticket_view, name='weighbridge_ticket'),
]
