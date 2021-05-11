from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from UserInfos.models import UserInfo
from Notifications.models import Notification
from Butterflies.models import *
from .serializers import *
import random


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

    def get(self, request, receiver_user_id):
        try:
            queryset = UserInteraction.objects.filter(receiver_user_id=receiver_user_id)
            serializer = UserInteractionSerializer(queryset, many=True)
            return Response(serializer.data)
        except UserInteraction.DoesNotExist:
            return Response({"error": "UserInteractions received by this user do not exist"}, status=status.HTTP_404_NOT_FOUND)

class UserInteractionsEndPointByReceiverAndNotifType(APIView):

    def get(self, request, receiver_user_id):
        try:
			#Reduce to notifications [user and global(id = 7)]
            queryset = UserInteraction.objects.filter(Q(receiver_user_id=receiver_user_id)
                                                     |Q(receiver_user_id=receiver_user_id)
                                                     &Q(user_interaction_type_id = 1))
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
        
# TODO: SuperFly session object to be created (POST), viewed (GET), and added to (PATCH)
class SuperflySessionEndpoint(APIView):
    def getRandomRecipe(self):
        recipeList = list(Superfly.objects.all())
        recipeIndex = random.randint(0, len(recipeList) - 1)
        return recipeList[recipeIndex]
    
    def inviteParticipants(self, new_session):
        default_uid = 2147483648
        #First grab 4 other users
        userList = list(UserInfo.objects.filter(user_id__lt=default_uid, user_superflysession_id=-1))
        print(userList)
        
        for i in range(1,5):
            #Invite four participants by creating invite objects linking them to this session.
            curr_invite = SuperflyInvite(session=new_session, )
            

    def get(self, request, session_id):
        try:
            #Possible refactor to eliminate explicitly define primary keys, as Django can autopopluate them for us. 
            session = SuperflySession.objects.get(session_id=session_id)
            serializer = SuperflySessionSerializer(queryset)
            return Response(serializer.data)
        except SuperflySession.DoesNotExist:
            return Response({"error": "UserInteractionType does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = SuperflySessionSerializer(data=request.data)
        if serializer.is_valid():
            #First init all fields to defaults
            new_session = SuperflySession()
            new_session = serializer.save()
            #Then set a random recipe and update with save(). 
            new_session.superfly_recipe = self.getRandomRecipe()
            new_session.save()
            
            print(new_session.superfly_recipe.superfly_name)

         #  print("Session superfly: %d", new_session.superfly_recipe.superfly_id)
            # We posted a session, so let's invite four other users to it.
            self.inviteParticipants(new_session)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, value):
        #Test
        print("Hello world")
    

    

    
