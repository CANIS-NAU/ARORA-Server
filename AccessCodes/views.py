from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_condition import Or

from .models import AccessCodes
from .serializers import AccessCodesSerializers
from UserInfos.models import UserInfo
from UserInfos.serializers import UserInfoSerializer

from django.db.utils import IntegrityError

# Get all access codes in db
class AllAccessCodes(APIView):
    permission_classes = [ AllowAny ]
    def get(self, request):
        queryset = AccessCodes.objects.all()
        serializer = AccessCodesSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Get all codes a given supervisor has created
class AllSupervisorGeneratedCodes( APIView ):
	def get( self , request , user_id ):
		try:
			userQuery = UserInfo.objects.get( user_id=user_id )
			userSerializer = UserInfoSerializer( userQuery )
			query = AccessCodes.objects.filter( creator_id=user_id )
			serializer = AccessCodesSerializers( query , many=True)
			return Response( serializer.data, status=status.HTTP_200_OK)
		except UserInfo.DoesNotExist:
			return Response({"error":"User does not exist"} , status=status.HTTP_404_NOT_FOUND)

class AccessCodeEndpoints( APIView ):
	#get a given access code information based on specific access code
	def get( self , request , access_code ):
		try:
			query = AccessCodes.objects.get( access_code=access_code )
			serializer = AccessCodesSerializers( query )
			return Response( serializer.data )
		except AccessCodes.DoesNotExist:
			return Response({"error":"This access code does not exist"} , status=status.HTTP_404_NOT_FOUND)
	#create an access code with all  given properties
	def post( self , request ):
		try:
                        access_code = request.data['access_code']
                        creator_id = request.data['creator_id']
                        created_at = request.data['created_at']
                        expired_at = request.data['expired_at']
                        authority_level = request.data['authority_level']
                        queryset = AccessCodes.objects.all()
                        serializer = AccessCodesSerializers(queryset, many=True)
			#check that the new access code is not already created
                        for code in serializer.data:
                          if code['access_code'] == access_code:
                            return Response({"error": "That access code already exists"}, status=status.HTTP_400_BAD_REQUEST)
		except KeyError:
			return Response({"error": "Wrong Json Format"}, status=status.HTTP_400_BAD_REQUEST)
		#Create and save new access code to db
		new_access_code = AccessCodes.objects.create(access_code=access_code, creator_id=creator_id ,
							 created_at=created_at , expired_at=expired_at, authority_level=authority_level)
		new_access_code.save()
		return Response({"Access Code": new_access_code.access_code}, status=status.HTTP_200_OK )

	#delete given access code
	def delete( self, request, access_code ):
		try:
			delete_access_code = AccessCodes.objects.get(access_code=access_code)
			delete_access_code.delete()
			return Response({"access code deleted"}, status=status.HTTP_200_OK)
		except AccessCodes.DoesNotExist:
			 return Response( {"error": "Access code does not exist"}, status=status.HTTP_404_NOT_FOUND)
