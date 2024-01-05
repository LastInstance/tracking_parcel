from django.urls import path
from . import views

urlpatterns = [
    path('check_address/', views.check_address, name='check_address'),
    path('create_parcel/', views.create_parcel, name='create_parcel'),
    path('change_parcel_status/<int:parcel_id>/', views.change_parcel_status, name='change_parcel_status'),
    path('check_parcel_status/<id:parcel_id/', views.check_parcel_status, name='check_parcel_status'),
    path('verify_email/', views.verify_email, name='verify_email'),
    path('get_all_results/', views.get_all_results, name='get_all_results'),
    path('get_result/<str:email>/', views.get_result, name='get_result'),
    path('delete_result/<str:email>/', views.delete_result, name='delete_result')

]