from django.urls import path

from . import views

urlpatterns = [
    path('notification/<int:notification_id>', views.NotificationEndPoint.as_view()),
    path('notification', views.NotificationEndPoint.as_view()),
    path('notifications/<int:notification_user_id>/<int:notification_type_id>', views.NotificationsEndPointByNotificationType.as_view()),
    path('notifications/<int:notification_user_id>', views.NotificationsEndPoint.as_view()),
]
