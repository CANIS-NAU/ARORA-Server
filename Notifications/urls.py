from django.urls import path

from . import views

urlpatterns = [
    # Gets a single Notification record based on notification_id
    #path('notification/<int:notification_id>', views.NotificationEndPoint.as_view()),
    # Gets all Notification records TODO: change to "notifications"
    #path('notification', views.NotificationEndPoint.as_view()),
    # TODO: Work in progress and not a working method: trying to use notification user id and type id to get a proper list of notifications a user should see
    # SHOULD take in a multi-variable query;
    # path('notification/<int:notification_user_id>/<int:notification_type_id>', views.NotificationsEndPointByNotificationType.as_view()),
    # Notifications filtered only by a user ID and public users
    path('notifications/', views.NotificationsEndPoint.as_view()),
    path('notifications/<int:notification_user_id>', views.NotificationsEndPointByUserId.as_view()),
    
    # Ability to update Notification Types
    #path('notificationtype/<int:notification_type_id>', views.NotificationTypeEndPoint.as_view()),
    #path('notificationtype', views.NotificationTypeEndPoint.as_view()),
    #path('notificationtypes', views.NotificationTypesEndPoint.as_view()),
]
