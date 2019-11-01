from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Notification
from .serializers import NotificationSerializer


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

    def get(self, request, notification_user_id):
        try:
            queryset = Notification.objects.all().exclude(notification_user_id=notification_user_id)
            serializer = NotificationSerializer(queryset, many=True)
            return Response(serializer.data)
        except Notification.DoesNotExist:
            return Response({"error": "Notification does not exist"}, status=status.HTTP_404_NOT_FOUND)


class NotificationsEndPointByNotificationType(APIView):

    def get(self, request, notification_user_id, notification_type_id):
        try:
            queryset = Notification.objects.filter(notification_type_id=notification_type_id).exclude(notification_user_id=notification_user_id)
            serializer = NotificationSerializer(queryset, many=True)
            return Response(serializer.data)
        except Notification.DoesNotExist:
            return Response({"error": "Notifications of this type do not exist"}, status=status.HTTP_404_NOT_FOUND)
