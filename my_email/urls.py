from django.urls import path

from . import views

urlpatterns = [
    path('api/my_email/read_list/', views.get_my_email_list, name="get_my_email_list_url"),
    path('api/my_email/read/<int:my_email_id>/', views.get_my_email_detail, name='get_my_email_detail_url'),
    path('api/my_email/create/', views.create_my_email, name="create_my_email_url"),
    path('api/my_email/delete/<int:my_email_id>/', views.delete_my_email, name='delete_my_email'),
    path('api/my_email/update/<int:my_email_id>/', views.update_my_email, name='update_my_email'),
]