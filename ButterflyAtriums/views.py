from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *



class UserSuperflyEndPoint(APIView):

    def get(self, request, user_id):
        try:
            superflies_qs = UserSuperfly.objects.filter(id_user=user_id)
            print(list(superflies_qs))
            serializer = UserSuperflySerializer(superflies_qs, many=True)
            return Response(serializer.data)
        except UserSuperfly.DoesNotExist:
            return Response({"error": "UserInteraction does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = TradeRequestSerializer(data=request.data)
        print("Posted new trade request")
        if serializer.is_valid():
            new_trade = TradeRequest()
            new_trade = serializer.save()
            new_trade.sender = UserInfo.objects.get(user_id=new_trade.uid_sender)
            new_trade.recipient = UserInfo.objects.get(user_id=new_trade.uid_recipient)
            new_trade.save()
            # Who needs to know about which user interactions?
            # Liking and comments should just between receiver and initiator
            # TODO make a notification that corresponds 
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    """def patch(self, request, user_interaction_id):
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
            return Response({}, status=status.HTTP_200_OK)"""

