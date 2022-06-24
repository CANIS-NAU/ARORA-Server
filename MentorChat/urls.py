from django.urls import path 
from . import views 

urlpatterns = [
    path( 'Message/<int:message_id>' , views.MessageEndPoints.as_view() ),
    path( 'Message' , views.MessageEndPoints.as_view() ),
    path( 'Messages/<str:convo_id>' , views.MessagesEndPoints.as_view() ),
    path( 'Messages' , views.MessagesEndPoints.as_view() )
]
