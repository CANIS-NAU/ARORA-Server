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
    
    def getAvailable(self, new_session):
        #This id excludes default superusers.
        default_uid = 2147483648
        #First grab 4 other users, don't need to consider host as he is already in the new session.
        userList = list(UserInfo.objects.filter(user_id__lt=default_uid, user_superflysession_id=-1))   

        #Check to see if we couldn't sample anyone. 
        return userList

    def sampleParticipants(self, num_available, userList):
        sampledParticipants = []
        #Cases needed here, depending on how many users are available. 
        #If there is not a single user to invite, send back False to give an HTTP error message code.
        if(num_available == 0):
            return False
        #If we have no edge case number, we can select up to six for all other cases.
        elif (num_available >= 6):
            sampledParticipants = random.sample(userList, 6)
        #Otherwise sample what we have. 
        else:
            sampledParticipants = random.sample(userList, num_available)
        return sampledParticipants

    

    def inviteParticipants(self, available_participants, new_session):
        #Otherwise get
        num_available = len(available_participants)
        sampledParticipants = self.sampleParticipants(num_available, available_participants)
        print("Chosen participants: ", sampledParticipants)
        
        #Now we know how many people to invite, send them. TODO: Race condition between clients?
        for i in range(0, num_available):
            print(sampledParticipants[i].user_superflysession_id)
            #Invite four participants by creating invite objects linking them to this session.
            #Only invite if we haven't already or they deleted it.
            curr_invite = SuperflyInvite(session=new_session, recipient=sampledParticipants[i], uid_recipiant = sampledParticipants[i].user_id)
            curr_invite.save()
        #Return True after we send the invites sucessfully
        return True

    def get(self, request, session_id):
        try:
            #Possible refactor to eliminate explicitly defined primary keys, as Django can autopopluate them for us. 
            sessionqs = SuperflySession.objects.get(session_id=session_id)
            serializer = SuperflySessionSerializer(sessionqs)
            return Response(serializer.data)
        except SuperflySession.DoesNotExist:
            return Response({"error": "UserInteractionType does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = SuperflySessionSerializer(data=request.data)
        print("Request user id: ", request.user)
        print("Serializer", serializer)
        if serializer.is_valid():
            print("Serializer is valid?")
            #First init all fields to defaults
            new_session = SuperflySession()
            new_session = serializer.save()

            
            
            #Get the record for the participant id that created the session. 
            
            participant_0 = UserInfo.objects.get(user_id = new_session.id_0) 
            
            #list(UserInfo.objects.filter(user_id=new_session.id_0))[0]
            participant_0.user_superflysession_id = new_session.session_id
            
            #Sets the userinfo model id
            #participant_0.user_superflysession_id = new_session.session_id
            #Save here to update the UserInfo model pointed at from participant_0
            #participant_0.save()
            print("Saving model" + str(participant_0.user_superflysession_id))
            new_session.participant_0 = participant_0
            #Save the participant_0 record to show they are trying to make a new session
                #We need to save here so getAvailable does not try to invite this user to their own session..
            participant_0.save()

            # We posted a session, so let's see if anyone is available to invite
            availableParticipants = self.getAvailable(new_session)

            #If this is true then we have no other players available, cancel the session and do not save the updated userinfo object!
            if(len(availableParticipants) == 0):
                #We need to undo the changes we made with another save as this session is not valid.
                participant_0.user_superflysession_id = 0
                participant_0.save()
                #Send the user an error to show we have no participants ready. 
                return Response({"error": serializer.errors}, status=status.HTTP_409_CONFLICT)

            #NOW invite other players
            self.inviteParticipants(availableParticipants, new_session)


            #Then set a random recipe for the session and update with save(). 
            new_session.superfly_recipe = self.getRandomRecipe()
            
            #If all checks pass, save the new session. 
            new_session.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print("Serializer not is valid")
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, input_session_id):
        #Get a session to update, if it exists. 
        try:
            updated_session = SuperflySession.objects.get(session_id=input_session_id)
        except UserInteraction.DoesNotExist:
            return Response({"error": "UserInteraction does not exist"}, status=status.HTTP_404_NOT_FOUND)
        #Found the session, so let's update it TODO.


class SuperflyInviteEndpoint(APIView):
    #Used to get all invites for the inputted userid. 
    def get(self, request, input_id):
        try:
            invite_qs = SuperflyInvite.objects.filter(recipent=input_id)
            serializer = SuperflyInviteSerializer(invite_qs, many=True)
            return Response(serializer.data)
        except SuperflyInvite.DoesNotExist:
            return Response({"error": "No invites present for this user"}, status=status.HTTP_404_NOT_FOUND)
    
