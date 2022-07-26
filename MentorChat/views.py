from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_condition import Or

from .models import Message
from .serializers import MessageSerializers
from UserInfos.models import UserInfo
from UserInfos.serializers import UserInfoSerializer

from django.db.utils import IntegrityError
from django.db.models import Q
import hashlib

class MessageList( generics.GenericAPIView ):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers


class MessageDetail( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers

#Get all messages between a sender and reveiver
class MessagesBetweenUsers( APIView ):
	def get( self , request , sender_id , receiver_id ):
		try:
			user1Query = UserInfo.objects.get( user_id=sender_id )
			user2Query = UserInfo.objects.get( user_id=receiver_id )
			#query for all messages where sender and receiver are either sender or receiver
			query = Message.objects.filter( Q( message_sender_id=sender_id) | Q(message_reciver_id=receiver_id) |
							Q( message_sender_id=receiver_id) | Q(message_reciver_id=sender_id ))
			serializer = MessageSerializers( query, many=True )
			#We need to create a new list here because the query wont give back the exact messages we need
			new_message_array = []
			# loop through given messages and check for needed fields and append to the new list
			for message in serializer.data:
				if message['message_sender_id'] == sender_id and message['message_reciver_id'] == receiver_id:
					new_message_array.append( message )
				elif message['message_sender_id'] == receiver_id and message['message_reciver_id'] == sender_id:
					new_message_array.append( message )
			#Return list of messages between two users
			return Response( new_message_array )
		except UserInfo.DoesNotExist:
			return Response( {"error": "One of the users does not exist"} , status=status.HTTP_404_NOT_FOUND )

#Get all messages the mentor has sent
class MentorChats( APIView ):
	def get( self , request , mentor_id ):
		try:
			userQuery = UserInfo.objects.get( user_id=mentor_id )
			userSerializer = UserInfoSerializer( userQuery )
			try:
				#Query for mentor id is either the sender or receiver
				query = Message.objects.filter(Q( message_sender_id=mentor_id) | Q( message_reciver_id=mentor_id ) )
				serializer = MessageSerializers( query, many=True )
				return Response( serializer.data )
			except Message.DoesNotExist:
				return Response( {"error": "Messsages with this mentor id does not exist"} , status=status.HTTP_404_NOT_FOUND )
		except UserInfo.DoesNotExist:
			return Response( {"error": "Messsages with this mentor id does not exist"}, status=status.HTTP_404_NOT_FOUND )
class MessageEndPoints( APIView ):
    def get( self , request , message_id ):
        try:
            #query for message with corresponding id and throw back the message data
            query = Message.objects.get( message_id=message_id )
            serializer = MessageSerializers( query )
            return Response( serializer.data )
        except Message.DoesNotExist:
            return Response( {"error": "Messsage with this id does not exist"} , status=status.HTTP_404_NOT_FOUND )
    #create a message object given the data
    def post( self , request ):
      try:
         message_text = request.data['message_text']
         message_date = request.data['message_date']
         message_sender_id = request.data['message_sender_id']
         sender_name = request.data['sender_name']
         reciver_id = request.data['message_reciver_id']

      except KeyError:
          return Response({"error": "Wrong Json Format"}, status=status.HTTP_400_BAD_REQUEST)
      #Generate a hashed message convo id using a md5 hash function
      hash_id1 = hashlib.md5( str( message_sender_id ).encode() + str( reciver_id ).encode() ).hexdigest()
      hash_id2 = hashlib.md5( str( reciver_id ).encode() + str( message_sender_id ).encode() ).hexdigest()
      #Check for convo id in use. Assign the one not in use and create message object. If neither in use,  defaults to hash_id1
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

    #delete a message based on the message id passed
    def delete( self, request, message_id):
        try:
            delete_message_id = Message.objects.get( message_id=message_id )
            delete_message_id.delete()
            return Response({"Message Successfully Deleted"}, status=status.HTTP_200_OK)
        except Message.DoesNotExist:
            return Response( {"error": "Message with that id does not exist"}, status=status.HTTP_404_NOT_FOUND)

#Get all messages with the given convo id
class MessagesEndPoints( APIView ):
	def get( self, request, convo_id ):
		try:
			queryset = Message.objects.filter( convo_id=convo_id )
			serializer = MessageSerializers( queryset, many=True )
			return Response( serializer.data )
		except Message.DoesNotExist:
			return Response({"error" : "Messages do not exist with that convo id"}, status=status.HTTP_404_NOT_FOUND)
