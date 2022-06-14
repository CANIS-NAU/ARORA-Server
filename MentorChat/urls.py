from django.urls import path 
from . import views 

urlpatterns = [
    path( 'Message/<int:messageId>' , views.MessageEndPoints.as_view() ),
    path( 'Message' , views.MessageEndPoints.as_view() )
]
