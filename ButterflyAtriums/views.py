from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *



class ButterflyAtriumEndPoint(APIView):

    def get(self, request, butterfly_atrium_id):
        try:
            query = ButterflyAtrium.objects.get(butterfly_atrium_id=butterfly_atrium_id)
            serializer = ButterflyAtriumSerializer(query)
            return Response(serializer.data)
        except ButterflyAtrium.DoesNotExist:
            return Response({"error": "User butterfly atrium does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = ButterflyAtriumSerializer(data=request.data)
        if serializer.is_valid():
            new_butterfly_atrium = serializer.save()
            return Response({"butterfly_atrium_id": new_butterfly_atrium.butterfly_atrium_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, butterfly_atrium_id):
        try:
            update_butterfly_atrium = ButterflyAtrium.objects.get(butterfly_atrium_id=butterfly_atrium_id)
        except ButterflyAtrium.DoesNotExist:
            return Response({"error": "Butterfly atrium does not exist"}, status=status.HTTP_404_NOT_FOUND)

        '''This code chunk uses to check if the request is form the user who creates this item'''
        # if update_user_butterfly.UserId != request.user:
        #     return Response({"error": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
        '''code chunk ends'''

        serializer = ButterflyAtriumSerializer(update_butterfly_atrium, data=request.data)
        if serializer.is_valid():
            update_butterfly_atrium = serializer.save()
            return Response({"butterfly_atrium_id": update_butterfly_atrium.butterfly_atrium_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, butterfly_atrium_id):
        try:
            delete_butterfly_atrium = ButterflyAtrium.objects.get(butterfly_atrium_id=butterfly_atrium_id)
            # if delete_user_butterfly.UserId.UserId != request.user.UserId:
            #     return Response({"error": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
            delete_butterfly_atrium.delete()
            return Response({}, status=status.HTTP_200_OK)
        except UserButterfly.DoesNotExist:
            return Response({"error": "User butterfly atrium does not exist"}, status=status.HTTP_404_NOT_FOUND)


class ButterflyAtriumEndPointByUserId(APIView):

    def get(self, request, butterfly_atrium_user_id):
        try:
            query = ButterflyAtrium.objects.get(butterfly_atrium_user_id=butterfly_atrium_user_id)
            serializer = ButterflyAtriumSerializer(query)
            return Response(serializer.data)
        except ButterflyAtrium.DoesNotExist:
            return Response({"error": "User butterfly atrium does not exist"}, status=status.HTTP_404_NOT_FOUND)

