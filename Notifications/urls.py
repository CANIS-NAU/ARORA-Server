from django.urls import path

from . import views

urlpatterns = [
    path('notification/<int:notification_id>', views.NotificationEndPoint.as_view()),
    path('notification', views.NotificationEndPoint.as_view()),
    path('notification/<int:notification_user_id>/<int:notification_type_id>', views.NotificationsEndPointByNotificationType.as_view()),
    path('notification/<int:notification_user_id>', views.NotificationsEndPoint.as_view()),

    #Trying to get the notification types page to show up and not have it stated as an error
    path('notificationtype/<int:notification_type_id>', views.NotificationTypeEndPoint.as_view()),
    path('notificationtype', views.NotificationTypeEndPoint.as_view()),
    path('notificationtypes', views.NotificationTypesEndPoint.as_view()),
    ]
