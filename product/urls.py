from django.urls import path

from . import views

urlpatterns = [
    path('api/products/', views.get_product_list, name="get_product_list_url"),
    path('api/products/<int:product_id>/', views.get_product_detail, name='get_product_detail_url'),
    path('api/products/create/', views.create_product, name="create_product_url"),
    path('api/product/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('api/product/update/<int:product_id>/', views.update_product, name='update_product'),
]