from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


#Methods accepted: POST, GET, (DELETE in the future?)
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
        serializer = UserSuperflySerializer(data=request.data)
        print("Posted new superfly request")
        if serializer.is_valid():
            new_user_superfly = serializer.save()
            print("Passed user_id: ", new_user_superfly.id_user)
            new_user_superfly.superfly = Superfly.objects.get(superfly_id=new_user_superfly.id_superfly)
            new_user_superfly.user = UserInfo.objects.get(user_id=new_user_superfly.id_user)
            
            new_user_superfly.save()
            #Everything created succesfully, then send the new superfly/user pairing back.
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    """# TODO add delete
    def delete(self, request, user_interaction_id):
            delete_user_interaction = UserInteraction.objects.get(user_interaction_id=user_interaction_id)
            if delete_user_interaction.UserId.UserId != request.user.UserId:
                return Response({"error": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
            delete_user_interaction.delete()
            return Response({}, status=status.HTTP_200_OK)"""

