from django.urls import path

from . import views

urlpatterns = [
    path('api/shippings/', views.get_shipping_list, name="get_shipping_list_url"),
    path('api/shippings/<int:shipping_id>/', views.get_shipping_detail, name='get_shipping_detail_url'),
    path('api/shippings/create/', views.create_shipping, name="create_shipping_url"),
    path('api/shipping/delete/<int:shipping_id>/', views.delete_shipping, name='delete_shipping'),
    path('api/shipping/update/<int:shipping_id>/', views.update_shipping, name='update_shipping'),
]