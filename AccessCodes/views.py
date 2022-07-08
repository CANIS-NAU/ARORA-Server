from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_condition import Or

from .models import AccessCodes
from .serializers import AccessCodesSerializers
from django.db.utils import IntegrityError

# Create your views here.
class AllAccessCodes(APIView):
    def get(self, request):
        queryset = AccessCodes.objects.all()
        serializer = AccessCodesSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AccessCodeEndpoints( APIView ):
	def get( self , request , access_code ):
		try:
			query = AccessCodes.objects.get( access_code=access_code )
			serializer = AccessCodesSerializers( query )
			return Response( serializer.data )
		except AccessCodes.DoesNotExist:
			return Response({"error":"This access code does not exist"} , status=status.HTTP_404_NOT_FOUND)

	def post( self , request ):
		try:
			access_code = request.data['access_code']
			creator_id = request.data['creator_id']
			created_at = request.data['created_at']
		except KeyError:
			return Response({"error": "Wrong Json Format"}, status=status.HTTP_400_BAD_REQUEST)
		new_access_code = AccessCodes.objects.create(access_code=access_code, creator_id=creator_id ,
							 created_at=created_at)
		return Response({"Access Code": new_access_code.access_code}, status=status.HTTP_200_OK )
	def delete( self, request, access_code ):
		try:
			delete_access_code = AccessCodes.objects.get(access_code=access_code)
			delete_access_code.delete()
			return Response({"access code deleted"}, status=status.HTTP_200_OK)
		except AccessCodes.DoesNotExist:
			 return Response( {"error": "Access code does not exist"}, status=status.HTTP_404_NOT_FOUND)
