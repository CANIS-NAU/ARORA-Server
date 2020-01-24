from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from UserInfos.models import UserInfo
from Notifications.models import Notification
from .serializers import *


class UserInteractionList(generics.ListAPIView):
    queryset = UserInteraction.objects.all()
    serializer_class = UserInteractionSerializer


class UserInteractionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserInteraction.objects.all()
    serializer_class = UserInteractionSerializer


class UserInteractionTypeEndPoint(APIView):

    def get(self, request, user_interaction_type_id):
        try:
            query = UserInteractionType.objects.get(user_interaction_type_id=user_interaction_type_id)
            serializer = UserInteractionTypeSerializer(query)
            return Response(serializer.data)
        except UserInteractionType.DoesNotExist:
            return Response({"error": "UserInteractionType does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = UserInteractionTypeSerializer(data=request.data)
        if serializer.is_valid():
            new_quest = serializer.save()
            return Response({"user_interaction_type_id": new_quest.user_interaction_type_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_interaction_type_id):
        try:
            updated_quest = UserInteractionType.objects.get(user_interaction_type_id=user_interaction_type_id)
        except UserInteractionType.DoesNotExist:
            return Response({"error": "UserInteractionType does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserInteractionTypeSerializer(updated_quest, data=request.data)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"user_interaction_type_id": updated_quest.user_interaction_type_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, user_interaction_type_id):
        try:
            updated_quest = UserInteractionType.objects.get(user_interaction_type_id=user_interaction_type_id)
        except UserInteractionType.DoesNotExist:
            return Response({"error": "UserInteractionType does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserInteractionTypeSerializer(updated_quest, data=request.data, partial=True)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"user_interaction_type_id": updated_quest.user_interaction_type_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserInteractionTypesEndPoint(APIView):

    def get(self, request):
        try:
            queryset = UserInteractionType.objects.all()
            serializer = UserInteractionTypeSerializer(queryset, many=True)
            return Response(serializer.data)
        except UserInteractionType.DoesNotExist:
            return Response({"error": "UserInteractionType does not exist"}, status=status.HTTP_404_NOT_FOUND)


class UserInteractionEndPoint(APIView):

    def get(self, request, user_interaction_id):
        try:
            query = UserInteraction.objects.get(user_interaction_id=user_interaction_id)
            serializer = UserInteractionSerializer(query)
            return Response(serializer.data)
        except UserInteraction.DoesNotExist:
            return Response({"error": "UserInteraction does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = UserInteractionSerializer(data=request.data)
        if serializer.is_valid():
            new_quest = serializer.save()
            # Who needs to know about which user interactions?
            # Liking and comments should just between receiver and initiator
            # TODO make a notification that corresponds 
            return Response({"user_interaction_id": new_quest.user_interaction_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_interaction_id):
        try:
            updated_quest = UserInteraction.objects.get(user_interaction_id=user_interaction_id)
        except UserInteraction.DoesNotExist:
            return Response({"error": "UserInteraction does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserInteractionSerializer(updated_quest, data=request.data)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"user_interaction_id": updated_quest.user_interaction_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, user_interaction_id):
        try:
            updated_quest = UserInteraction.objects.get(user_interaction_id=user_interaction_id)
        except UserInteraction.DoesNotExist:
            return Response({"error": "UserInteraction does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserInteractionSerializer(updated_quest, data=request.data, partial=True)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"user_interaction_id": updated_quest.user_interaction_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # TODO add delete
    def delete(self, request, user_interaction_id):
            delete_user_interaction = UserInteraction.objects.get(user_interaction_id=user_interaction_id)
            if delete_user_interaction.UserId.UserId != request.user.UserId:
                return Response({"error": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
            delete_user_interaction.delete()
            return Response({}, status=status.HTTP_200_OK)


class UserInteractionsEndPoint(APIView):

    def get(self, request):
        try:
            queryset = UserInteraction.objects.all()
            serializer = UserInteractionSerializer(queryset, many=True)
            return Response(serializer.data)
        except UserInteraction.DoesNotExist:
            return Response({"error": "UserInteraction does not exist"}, status=status.HTTP_404_NOT_FOUND)

class UserInteractionsEndPointByInitiator(APIView):

    def get(self, request, initiator_user_id):
        try:
            queryset = UserInteraction.objects.filter(initiator_user_id=initiator_user_id)
            serializer = UserInteractionSerializer(queryset, many=True)
            return Response(serializer.data)
        except UserInteraction.DoesNotExist:
            return Response({"error": "UserInteractions initiated by this user do not exist"}, status=status.HTTP_404_NOT_FOUND)

class UserInteractionsEndPointByInitiatorAndNotifType(APIView):

    def get(self, request, initiator_user_id):
        try:
            queryset = UserInteraction.objects.filter(initiator_user_id=initiator_user_id)
            #Notifications are UserInteractionType 1. 
            queryset = queryset.filter(user_interaction_type_id=1)#Need to add a filter to get likes
            serializer = UserInteractionSerializer(queryset, many=True)
            return Response(serializer.data)
        except UserInteraction.DoesNotExist:
            return Response({"error": "UserInteractions initiated by this user do not exist"}, status=status.HTTP_404_NOT_FOUND)

class UserInteractionsEndPointByReceiver(APIView):

    def get(self, request, receiver_user_id, broadcast_user_id):
        try:
            queryset = UserInteraction.objects.filter(receiver_user_id=receiver_user_id)
            serializer = UserInteractionSerializer(queryset, many=True)
            return Response(serializer.data)
        except UserInteraction.DoesNotExist:
            return Response({"error": "UserInteractions received by this user do not exist"}, status=status.HTTP_404_NOT_FOUND)

class UserInteractionsEndPointByQuestReportId(APIView):

    def get(self, request, quest_report_id):
        try:
            queryset = UserInteraction.objects.filter(quest_report_id=quest_report_id)
            serializer = UserInteractionSerializer(queryset, many=True)
            return Response(serializer.data)
        except UserInteraction.DoesNotExist:
            return Response({"error": "This QuestReport does not have any associated UserInteractions"}, status=status.HTTP_404_NOT_FOUND)
        
# TODO: Multiuser interaction where there is one initiator to many receivers (up to 6)
