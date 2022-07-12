from django.urls import path
from . import views

urlpatterns = [
    path( 'Message/<int:message_id>' , views.MessageEndPoints.as_view() ),
    path( 'MentorChats/<int:mentor_id>', views.MentorChats.as_view() ),
    path( 'MessagesBetweenUsers/<int:sender_id>/<int:receiver_id>', views.MessagesBetweenUsers.as_view()),
    path( 'Message' , views.MessageEndPoints.as_view() ),
    path( 'Messages/<str:convo_id>' , views.MessagesEndPoints.as_view() ),
    path( 'Messages' , views.MessagesEndPoints.as_view() )
]
