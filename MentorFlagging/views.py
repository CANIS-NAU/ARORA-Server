from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_condition import Or

from .models import Flagging
from .serializers import FlaggingSerializer
from UserInfos.models import UserInfo
from UserInfos.serializers import UserInfoSerializer

class AllMentorFlags( APIView ):
	def get( self, request, mentor_id ):
		try:
			userQuery = UserInfo.objects.get( user_id=mentor_id )
			userSerializer = UserInfoSerializer( userQuery )
			try:
				query = Flagging.objects.filter( mentor_id=mentor_id)
				serializer = FlaggingSerializer( query )
				return Response( serializer.data )
			except Flagging.DoesNotExist:
				return Response( {"error": "No Flags"} , status=status.HTTP_404_NOT_FOUND )
		except UserInfo.DoesNotExist:
			return Response( {"error": "User with this mentee id does not exist"}, status=status.HTTP_404_NOT_FOUND )

class FlaggingEndpoints( APIView ):
	#get all flags on mentee
	def get( self, request, mentee_id ):
		try:
			userQuery = UserInfo.objects.get( user_id=mentee_id )
			userSerializer = UserInfoSerializer( userQuery )
			try:
				query = Flagging.objects.filter( mentee_id=mentee_id)
				serializer = FlaggingSerializer( query )
				return Response( serializer.data )
			except Flagging.DoesNotExist:
				return Response( {"error": "No Flags"} , status=status.HTTP_404_NOT_FOUND )
		except UserInfo.DoesNotExist:
			return Response( {"error": "User with this mentee id does not exist"}, status=status.HTTP_404_NOT_FOUND )
	#create a new flag on a user
	def post( self, request ):
		try:
			mentee_id = request.data["mentee_id"]
			mentor_id = request.data["mentor_id"]
			timestamp_flagged = request.data["timestamp_flagged"]
			timestamp_resolved = request.data["timestamp_resolved"]
			reason_flagged = request.data["reason_flagged"]
			how_resolved = request.data["how_resolved"]
		except KeyError:
			return Response({"error": "Wrong Json Format"}, status=status.HTTP_400_BAD_REQUEST)
		new_flag = Flagging.objects.create( mentee_id=mentee_id, mentor_id=mentor_id, timestamp_flagged=timestamp_flagged, timestamp_resolved=timestamp_resolved,reason_flagged=reason_flagged, how_resolved=how_resolved )
		new_flag.save()
		return Response({"Flag created successfully"}, status=status.HTTP_200_OK )

	def patch( self, request, id ):
		try:
			flag = Flagging.objects.get( id=id )
		except Flagging.DoesNotExist:
			return Response({"error": "Flag with that id does not exist"}, status=status.HTTP_404_NOT_FOUND)
		serializer = FlaggingSerializer( flag, data=request.data, partial=True )
		if serializer.is_valid():
			flag = serializer.save()
			return Response({"successful"}, status=status.HTTP_200_OK)
		return Response({"error": "Wrong Json Format"}, status=status.HTTP_404_BAD_REQUEST)
