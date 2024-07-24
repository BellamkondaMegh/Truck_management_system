
from django.urls import path
from django.contrib import admin
from trucks.views import weighbridge_ticket
from trucks.views import truck_list, add_truck,truck_detail, material_list, ticket_list, ticket_detail, download_ticket,home,register, user_login, user_logout

urlpatterns = [
    path('admin/',admin.site.urls),
    
    path('weighbridge_ticket/', weighbridge_ticket, name='weighbridge_ticket'),
    path('home/', home),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add_truck/',add_truck, name='add_truck'),
    path('trucks/', truck_list, name='truck_list'),
    path('trucks/<int:pk>/', truck_detail, name='truck_detail'),
    path('materials/', material_list, name='material_list'),
    path('tickets/', ticket_list, name='ticket_list'),
    path('tickets/<int:pk>/', ticket_detail, name='ticket_detail'),
    path('tickets/<int:pk>/download/', download_ticket, name='download_ticket'),
]


