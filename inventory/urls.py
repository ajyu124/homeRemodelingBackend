from django.urls import path

from . import views

urlpatterns = [
    path('api/inventory/', views.get_inventory_list, name="get_inventory_list_url"),
    path('api/inventory/<int:inventory_id>/', views.get_inventory_detail, name='get_inventory_detail_url'),
    path('api/inventory/create/', views.create_inventory, name="create_inventory_url"),
    path('api/inventory/delete/<int:inventory_id>/', views.delete_inventory, name='delete_inventory'),
    path('api/inventory/update/<int:inventory_id>/', views.update_inventory, name='update_inventory'),
]