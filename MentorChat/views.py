from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_condition import Or
from .models import Message
from .serializers import MessageSerializers
from django.db.utils import IntegrityError
from django.db.models import Q
import hashlib

class MessageList( generics.GenericAPIView ):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers


class MessageDetail( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers

class MessagesBetweenUsers( APIView ):
	def get( self , request , sender_id , receiver_id ):
		try:
			query = Message.objects.filter( Q( message_sender_id=sender_id) | Q(message_reciver_id=receiver_id) or
							Q( message_sender_id=receiver_id) | Q(message_reciver_id=sender_id ))
			serializer = MessageSerializers( query, many=True )
			new_message_array = []
			for message in serializer.data:
				if message['message_sender_id'] == sender_id and message['message_reciver_id'] == receiver_id:
					new_message_array.append( message )
				elif message['message_sender_id'] == receiver_id and message['message_reciver_id'] == sender_id:
					new_message_array.append( message )
			return Response( new_message_array )
		except Message.DoesNotExist:
			return Response( {"error": "Messsages with these sender and reciever do not exist"} , status=status.HTTP_404_NOT_FOUND )


class MentorChats( APIView ):
	def get( self , request , mentor_id ):
		try:
			query = Message.objects.filter(Q( message_sender_id=mentor_id) | Q( message_reciver_id=mentor_id ) )
			serializer = MessageSerializers( query, many=True )
			return Response( serializer.data )
		except Message.DoesNotExist:
			return Response( {"error": "Messsages with this mentor id does not exist"} , status=status.HTTP_404_NOT_FOUND )

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
      try:
         message_text = request.data['message_text']
         message_date = request.data['message_date']
         message_sender_id = request.data['message_sender_id']
         sender_name = request.data['sender_name']
         reciver_id = request.data['message_reciver_id']

      except KeyError:
          return Response({"error": "Wrong Json Format"}, status=status.HTTP_400_BAD_REQUEST)

      hash_id1 = hashlib.md5( str( message_sender_id ).encode() + str( reciver_id ).encode() ).hexdigest()
      hash_id2 = hashlib.md5( str( reciver_id ).encode() + str( message_sender_id ).encode() ).hexdigest()
      try:
         query = Message.objects.filter( convo_id=hash_id1 )
         convo_id = hash_id1
      except Message.DoesNotExist:
             try:
                query = Message.objects.filter( convo_id=hash_id2 )
                convo_id = hash_id2
             except Message.DoesNotExist:
                convo_id = hash_id1

      new_message_convo = Message.objects.create( convo_id=convo_id, message_text=message_text,
                                                 message_date=message_date, message_sender_id=message_sender_id,
                                                 message_reciver_id=reciver_id, sender_name=sender_name )
      new_message_convo.save()
      return Response({"Convo Id": new_message_convo.convo_id}, status=status.HTTP_200_OK )

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


class MessagesEndPoints( APIView ):
	def get( self, request, convo_id ):
		convo_id = str( convo_id )
		try:
			queryset = Message.objects.filter( convo_id=convo_id )
			serializer = MessageSerializers( queryset, many=True )
			return Response( serializer.data )
		except Message.DoesNotExist:
			return Response({"error" : "All messages do not exist"}, status=status.HTTP_404_NOT_FOUND)
