from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


# Notification Types (object list ids start at 1)
# --1: Likes
# --2: Comments
# --3: Quest Report
# --4: Invitation
# --5: Task Alerts

#TODO Create endpoint for NotificationType

class NotificationList(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationEndPoint(APIView):

    def get(self, request, notification_id):
        try:
            query = Notification.objects.get(notification_id=notification_id)
            serializer = NotificationSerializer(query)
            return Response(serializer.data)
        except Notification.DoesNotExist:
            return Response({"error": "Notification does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            new_quest = serializer.save()
            return Response({"notification_id": new_quest.notification_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, notification_id):
        try:
            updated_quest = Notification.objects.get(notification_id=notification_id)
        except Notification.DoesNotExist:
            return Response({"error": "Notification does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = NotificationSerializer(updated_quest, data=request.data)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"notification_id": updated_quest.notification_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, notification_id):
        try:
            updated_quest = Notification.objects.get(notification_id=notification_id)
        except Notification.DoesNotExist:
            return Response({"error": "Notification does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = NotificationSerializer(updated_quest, data=request.data, partial=True)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"notification_id": updated_quest.notification_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class NotificationsEndPoint(APIView):
    def post(self, request):
        try:
            # Likes, comments, invitations; (excludes QuestReports[id 3] only)
            queryset = Notification.objects.all().exclude(notification_type_id=3)
            # TODO Get a second queryset that has all the quest reports that are complete
            # notifications about QuestReports (M1-M3)
            serializer = NotificationSerializer(queryset, many=True)
            return Response(serializer.data)
        except Notification.DoesNotExist:
            return Response({"error": "Notification does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        try:
            # Likes, comments, invitations; (excludes QuestReports[id 3] only)
            queryset = Notification.objects.all().exclude(notification_user_id=3)
            # TODO Get a second queryset that has all the quest reports that are complete
            # notifications about QuestReports (M1-M3)

            with open("debug.txt", "a") as fo:
                fo.write("%s\n" % queryset)

            serializer = NotificationSerializer(queryset, many=True)
            return Response(serializer.data)
        except Notification.DoesNotExist:
            return Response({"error": "Notification does not exist"}, status=status.HTTP_404_NOT_FOUND)

class NotificationsEndPointByUserId(APIView):
    def post(self, request, notification_user_id):
        try:

            # Filter the query set by the URL parameters
            queryset_user_id=list(Notification.objects.all().filter(notification_user_id=notification_user_id))
            queryset_user_public=list(Notification.objects.all().filter(notification_user_id=7))

            # Merge queryset
            queryset=queryset_user_id + queryset_user_public
            with open("debug.txt", "a") as fo:
                fo.write("%s\n" % queryset)

            # Serialize and return as formatted RESPONSE
            serializer=NotificationSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Notification.DoesNotExist:
            return Response({"error": "Notification does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, notification_user_id):
        try:

            # Filter the query set by the URL parameters
            queryset_user_id=list(Notification.objects.all().filter(notification_user_id=notification_user_id))
            queryset_user_public=list(Notification.objects.all().filter(notification_user_id=7))

            # Merge queryset
            queryset=queryset_user_id + queryset_user_public
            #QuerySet(queryset)
            print(queryset)
            with open("debug.txt", "a") as fo:
                fo.write("%s\n" % queryset)

            # Serialize and return as formatted RESPONSE
            serializer=NotificationSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Notification.DoesNotExist:
            return Response({"error": "Notification does not exist"}, status=status.HTTP_404_NOT_FOUND)

class NotificationTypeEndPoint(APIView):

    def get(self, request, notification_type_id):
        try:
            query = NotificationType.objects.get(notification_type_id=notification_type_id)
            serializer = NotificationTypeSerializer(query)
            return Response(serializer.data)
        except NotificationType.DoesNotExist:
            return Response({"error": "NotificationType does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = NotificationTypeSerializer(data=request.data)
        if serializer.is_valid():
            new_quest = serializer.save()
            return Response({"notification_type_id": new_quest.notification_type_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, notification_type_id):
        try:
            updated_quest = NotificationType.objects.get(notification_type_id=notification_type_id)
        except NotificationType.DoesNotExist:
            return Response({"error": "NotificationType does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = NotificationTypeSerializer(updated_quest, data=request.data)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"notificaiton_type_id": updated_quest.notificaiton_type_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, notification_type_id):
        try:
            updated_quest = NotificationType.objects.get(notification_type_id=notification_type_id)
        except NotificationType.DoesNotExist:
            return Response({"error": "NotificationType does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = NotificationTypeSerializer(updated_quest, data=request.data, partial=True)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"notification_type_id": updated_quest.notification_type_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#Current attempt to get all the notification types show up on the website
class NotificationTypesEndPoint(APIView):

    def get(self, request):
        try:
            queryset = NotificationType.objects.all()
            serializer = NotificationTypeSerializer(queryset, many=True)
            return Response(serializer.data)
        except NotificationType.DoesNotExist:
            return Response({"error": "NotificationType does not exist"}, status=status.HTTP_404_NOT_FOUND)


class NotificationsEndPointByNotificationType(APIView):
    # Types
    # --
    # --
    # --
    def get(self, request):
        try:
            # Get all of the notifications
            queryset = Notification.objects.all()

            # Get the specific parameters from the URL
            notification_type_id=self.request.query_params.get('notification_type_id')
            notification_user_id=self.request.query_params.get('notification_user_id')

            # Filter the query set by the URL parameters
            queryset=queryset.filter(notification_user_id=notification_user_id)
            queryset=queryset.filter(notification_type_id=notification_type_id)

            # Serialize and return as formatted RESPONSE
            serializer=NotificationSerializer(queryset, many=True)
            return Response(serializer.data)
        except Notification.DoesNotExist:
            return Response({"error": "Notifications of this type do not exist"}, status=status.HTTP_404_NOT_FOUND)


