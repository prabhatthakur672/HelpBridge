from django.urls import path
from . import views
urlpatterns = [
    path('request_list', views.request_list, name="request_list"),
    path('create_request', views.create_request, name="create_request"),
    path('edit_request/<int:req_id>', views.edit_request, name="edit_request"),
    path('delete_request/<int:req_id>', views.delete_request, name="delete_request"),
    path('register/', views.register, name='register'),
    path('offer_help/<int:req_id>', views.offer_help, name='offer_help'),
    path('offer_help_details/<int:req_id>', views.offer_help_details, name='offer_help_details'),
    path('profile/<int:user_id>', views.user_profile, name='user_profile'),
    path('notifications/', views.notifications, name='notifications'),
    path('mark_notification_as_read/<int:notification_id>/', views.mark_notification_as_read, name='mark_notification_as_read'),
    path('request_history/<int:request_id>/', views.request_history, name='request_history'),
    path('about-us', views.aboutUs, name='about'),
    path('contact', views.contactUs, name='contact'),

]