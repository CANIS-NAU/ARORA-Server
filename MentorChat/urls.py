from django.urls import path 
from . import views 

urlpatterns = [
    path( 'Messages/<int:messageId>' , views.MessageEndPoint.as_view() ),
]
