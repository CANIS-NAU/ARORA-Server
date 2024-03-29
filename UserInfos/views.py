from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny
from rest_condition import Or

from .utils import euclidean_distance
from .models import UserInfo
from MoodReports.models import MoodType
from Butterflies.models import UserButterfly
from .serializers import UserInfoSerializer, UserSerializer

from django.db.utils import IntegrityError
import math

class UserInfoList(generics.GenericAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class UserInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


# To be restricted to access,use for test
class UserList(generics.ListAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer

# Open Post request in UserInfo endpoint for all to register
class IsPostRequest(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST'


#   WARNING: Don't delete unused parameter.
class AllUserInfos(APIView):
    def get(self, request):
        queryset = UserInfo.objects.all()
        serializer = UserInfoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Get the app supervisor( only allows for 1 )
class Supervisor( APIView ):
	def get( self , request ):
		query = UserInfo.objects.get(user_type='supervisor')
		serializer = UserInfoSerializer( query ) #pass many=true if multiple supervisors
		return Response(serializer.data, status=status.HTTP_200_OK)

#get a list of unassigned mentees
class UnassignedMenteeList( APIView ):
	def get( self, request , user_id ):
		try:
			#Make sure the user Id correspondes to the supervisor
			supervisor = UserInfo.objects.get(user_id=user_id)
			supervisor_serializer = UserInfoSerializer( supervisor )
			if supervisor_serializer.data['user_type'] != 'supervisor':
				return Response({"error": "User not a supervisor"}, status=status.HTTP_400_BAD_REQUEST)
			#if unassigned then mentee has mentor id of supervisor. Return that list
			query = UserInfo.objects.filter(mentor_id=user_id)
			serializer = UserInfoSerializer( query, many=True)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except UserInfo.DoesNotExist:
			return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

#Get all mentors assigned mentees
class MentorAssignedList( APIView ):
	def get( self, request, mentor_id ):
		try:
			checkUser = UserInfo.objects.get( user_id=mentor_id )
			checkUserSerializer = UserInfoSerializer( checkUser)
			query = UserInfo.objects.filter(mentor_id=mentor_id)
			serializer = UserInfoSerializer( query, many=True )
			return Response(serializer.data, status=status.HTTP_200_OK)
		except UserInfo.DoesNotExist:
			return Response({"error": "Mentor id invalid"}, status=status.HTTP_404_NOT_FOUND)

#Change a mentees mentor
class ChangeAssignedMentor( APIView ):
	def patch( self , request , user_id ):
		try:
			update_user = UserInfo.objects.get( user_id=user_id )
		except UserInfo.DoesNotExist:
			 return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
		serializer = UserInfoSerializer(update_user, data=request.data, partial=True)
		if serializer.is_valid():
			update_user = serializer.save()
			return Response({"user_id": update_user.user_id}, status=status.HTTP_200_OK)
		return Response({"error": "Wrong Json Format"}, status=status.HTTP_400_BAD_REQUEST)

class CreateUser( APIView ):
    permission_classes = [ AllowAny ]
    def post(self, request):
        try:
            username = request.data['username']
            email = request.data['email']
            password = request.data['password']
        except KeyError:
            return Response({"error": "Wrong Json Format"}, status=status.HTTP_409_CONFLICT)
        try:
            new_user = UserInfo.objects.create_user(username=username, email=email, password=password)
            new_user.user_id = new_user.user_info_id
            new_user.save()
            return Response({"user_id": new_user.user_id}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({"error": "User already exists with this user_name and/or email"},
                            status=status.HTTP_409_CONFLICT)


class UserInfos(APIView):
    def get(self, request, user_id):
        try:
            query = UserInfo.objects.get(user_id=user_id)
            serializer = UserInfoSerializer(query)
            return Response(serializer.data)
        except UserInfo.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, user_id):
        try:
            updated_user = UserInfo.objects.get(user_id=user_id)
        except UserInfo.DoesNotExist:
            return Response({"error": "User_id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        '''The code chunk below uses to check if user_current_mood&user_current_butterfly in the request is valid data 
        by looking up the corresponding table, MoodType&UserButterfly'''

        # try:
        #     user_current_mood = request.data['user_current_mood']
        #     user_current_butterfly = request.data['user_current_butterfly']
        # except KeyError:
        #     return Response({"error": "Wrong Json Format"}, status=status.HTTP_400_BAD_REQUEST)
        #
        # try:
        #     MoodType.objects.get(MoodTypeId=user_current_mood)
        # except MoodType.DoesNotExist:
        #     return Response({"error": "Mood_type does not exist"}, status=status.HTTP_404_NOT_FOUND)
        #
        # try:
        #     UserButterfly.objects.get(UserButterflyId=user_current_butterfly)
        # except UserButterfly.DoesNotExist:
        #     return Response({"error": "User_butterfly does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # if update_user_butterfly.UserId != request.user:
        #     return Response({"error": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
        '''The code chunk ends here'''

        serializer = UserInfoSerializer(updated_user, data=request.data)
        if serializer.is_valid():
            updated_user = serializer.save()
            return Response({"user_id": updated_user.user_id}, status=status.HTTP_200_OK)
        return Response({"error": "Wrong Json Format"}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, user_id):
        try:
            updated_user = UserInfo.objects.get(user_id=user_id)
        except UserInfo.DoesNotExist:
            return Response({"error": "User_id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        '''The code chunk below uses to check if user_current_mood&user_current_butterfly in the request is valid data 
        by looking up the corresponding table, MoodType&UserButterfly'''

        # try:
        #     user_current_mood = request.data['user_current_mood']
        #     user_current_butterfly = request.data['user_current_butterfly']
        # except KeyError:
        #     return Response({"error": "Wrong Json Format"}, status=status.HTTP_400_BAD_REQUEST)
        #
        # try:
        #     MoodType.objects.get(MoodTypeId=user_current_mood)
        # except MoodType.DoesNotExist:
        #     return Response({"error": "Mood_type does not exist"}, status=status.HTTP_404_NOT_FOUND)
        #
        # try:
        #     UserButterfly.objects.get(UserButterflyId=user_current_butterfly)
        # except UserButterfly.DoesNotExist:
        #     return Response({"error": "User_butterfly does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # if update_user_butterfly.UserId != request.user:
        #     return Response({"error": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
        '''The code chunk ends here'''

        serializer = UserInfoSerializer(updated_user, data=request.data, partial=True)
        if serializer.is_valid():
            updated_user = serializer.save()
            return Response({"user_id": updated_user.user_id}, status=status.HTTP_200_OK)
        return Response({"error": "Wrong Json Format"}, status=status.HTTP_400_BAD_REQUEST)

class NearByUser(APIView):

    def get(self, request, user_id):
        near_by_list = []
        try:
            the_request_user = UserInfo.objects.get(user_id=user_id)
            the_user_set = UserInfo.objects.all()
            for user in the_user_set:
                if euclidean_distance(the_request_user.user_current_location_lat,
                                      the_request_user.user_current_location_long,
                                      user.user_current_location_lat,
                                      user.user_current_location_long):
                    near_by_list.append(user)

            serializer = UserInfoSerializer(near_by_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserInfo.DoesNotExist:
            return Response({"error": "User  does not exist"}, status=status.HTTP_404_NOT_FOUND)
