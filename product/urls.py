from django.urls import path

from . import views
from . import views_image_upload

urlpatterns = [
    path('api/product/read_list/', views.get_product_list, name="get_product_list_url"),
    
    path('api/product/read/<int:product_id>/', views.get_product_detail, name='get_product_detail_url'),
    path('api/product/create/', views.create_product, name="create_product_url"),
    path('api/product/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('api/product/update/<int:product_id>/', views.update_product, name='update_product'),

    path('api/product/image_upload/', views_image_upload.ImageUploadView.as_view(), name='image-upload'),
    path('api/images/<str:filename>/', views_image_upload.serve_uploaded_image, name='serve-uploaded-image'),
]