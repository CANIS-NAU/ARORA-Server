from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_condition import Or

from .models import Message
from .serializers import MessageSerializers
from django.db.utils import IntegrityError


class MessageList( generics.GenericAPIView ):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers


class MessageDetail( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers

class MessageEndPoints( APIView ):
    def get( self , request , message_id ):
        # Get the query string from db and throw back data that was obtained
        try:
            query = Message.objects.get( message_id=message_id )
            serializer = MessageSerializers( query ) #Might need to pass parameter many=true
            return Response( serializer.data )
        except Message.DoesNotExist:
            return Response( {"error": "Messsage with this id does not exist"} , status=status.HTTP_404_NOT_FOUND )

    def post( self , request ):
        # Grab the serializer for given incomming data
        serializer = MessageSerializers( data=request.data )
        # Check that all fields in the request are valid
        if serializer.is_valid():
            #Save the message in the db and return success
            new_message = serializer.save()
            return Response( {"Message ID": new_message.message_id}, status=status.HTTP_200_OK )
        return Response( {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST )

    def delete( self, request, message_id):
        try:
            # Obtain the message with the given id
            delete_message_id = Message.objects.get( message_id=message_id )
            # Delete and return sucess
            delete_message_id.delete()
            return Response({"Message Successfully Deleted"}, status=status.HTTP_200_OK)
        except Message.DoesNotExist:
            # Return unsuccessful
            return Response( {"error": "Message with that id does not exist"}, status=status.HTTP_404_NOT_FOUND)

# Check if we need PUT and PATCH requests
