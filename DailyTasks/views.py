from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import F
from .models import *
from UserInfos.models import UserInfo
from .serializers import *


class DailyTaskList(generics.ListAPIView):
    queryset = DailyTask.objects.all()
    serializer_class = DailyTaskSerializer


class DailyTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyTask.objects.all()
    serializer_class = DailyTaskSerializer



class DailyTaskEndPoint(APIView):

    def get(self, request, daily_task_id):
        try:
            query = DailyTask.objects.get(daily_task_id=daily_task_id)
            serializer = DailyTaskSerializer(query)
            return Response(serializer.data)
        except DailyTask.DoesNotExist:
            return Response({"error": "DailyTask does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = DailyTaskSerializer(data=request.data)
        if serializer.is_valid():
            new_quest = serializer.save()
            return Response({"daily_task_id": new_quest.daily_task_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, daily_task_id):
        try:
            updated_quest = DailyTask.objects.get(daily_task_id=daily_task_id)
        except DailyTask.DoesNotExist:
            return Response({"error": "DailyTask does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DailyTaskSerializer(updated_quest, data=request.data)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"daily_task_id": updated_quest.daily_task_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, daily_task_id):
        try:
            updated_quest = DailyTask.objects.get(daily_task_id=daily_task_id)
        except DailyTask.DoesNotExist:
            return Response({"error": "DailyTask does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DailyTaskSerializer(updated_quest, data=request.data, partial=True)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"daily_task_id": updated_quest.daily_task_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class DailyTasksEndPoint(APIView):

    def get(self, request):
        try:
            queryset = DailyTask.objects.all()
            serializer = DailyTaskSerializer(queryset, many=True)
            return Response(serializer.data)
        except DailyTask.DoesNotExist:
            return Response({"error": "DailyTask does not exist"}, status=status.HTTP_404_NOT_FOUND)

class UserInteractionsEndPointByUserId(APIView):

    def get(self, request, daily_task_user_id):
        try:
            queryset = DailyTask.objects.get(daily_task_user_id=daily_task_user_id)
            serializer = DailyTaskSerializer(queryset, many=True)
            return Response(serializer.data)
        except DailyTask.DoesNotExist:
            return Response({"error": "DailyTasks initiated by this user do not exist"}, status=status.HTTP_404_NOT_FOUND)

class DailyTasksEndPointByComplete(APIView):

    def get(self, request, daily_task_day):
        try:
            queryset = DailyTask.objects.filter(daily_task_likes_achieved__gte=F('daily_task_likes_required')).filter(daily_task_butterflies_achieved__gte=F('daily_task_butterflies_required')).filter(daily_task_m1_achieved__gte=F('daily_task_m1_required')).filter(daily_task_m2_achieved__gte=F('daily_task_m2_required')).filter(daily_task_m3_achieved__gte=F('daily_task_m3_required')).exclude(daily_task_day__lt=datetime.date.today())

            serializer = DailyTaskSerializer(queryste, many=True)
            return Response(serializer.data)
        except DailyTask.DoesNotExist:
            return Response({"error": "There are no DailyTasks that are complete"}, status=status.HTTP_404_NOT_FOUND)
