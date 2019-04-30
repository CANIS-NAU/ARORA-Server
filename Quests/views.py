from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from .models import *
from .serializers import *


class QuestStatusEndPoint(APIView):

    def get(self, request, quest_status_id):
        try:
            query = QuestStatus.objects.get(quest_status_id=quest_status_id)
            serializer = QuestStatusSerializer(query)
            return Response(serializer.data)
        except QuestStatus.DoesNotExist:
            return Response({"error": "Quest_status does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = QuestStatusSerializer(data=request.data)
        if serializer.is_valid():
            new_quest_status = serializer.save()
            return Response({"quest_status_id": new_quest_status.quest_status_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, quest_status_id):
        try:
            updated_quest_status = QuestStatus.objects.get(quest_status_id=quest_status_id)
        except QuestStatus.DoesNotExist:
            return Response({"error": "Quest_status does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuestStatusSerializer(updated_quest_status, data=request.data)
        if serializer.is_valid():
            updated_quest_status = serializer.save()
            return Response({"quest_status_id": updated_quest_status.quest_status_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, quest_status_id):
        try:
            updated_phrase = QuestStatus.objects.get(quest_status_id=quest_status_id)
        except QuestStatus.DoesNotExist:
            return Response({"error": "Quest_status does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuestStatusSerializer(updated_phrase, data=request.data, partial=True)
        if serializer.is_valid():
            updated_phrase = serializer.save()
            return Response({"quest_status_id": updated_phrase.quest_status_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class QuestStatusesEndPoint(APIView):

    def get(self, request):
        try:
            queryset = QuestStatus.objects.all()
            serializer = QuestStatusSerializer(queryset, many=True)
            return Response(serializer.data)
        except QuestStatus.DoesNotExist:
            return Response({"error": "QuestStatus does not exist"}, status=status.HTTP_404_NOT_FOUND)


class QuestTypeEndPoint(APIView):

    def get(self, request, quest_type_id):
        try:
            query = QuestType.objects.get(quest_type_id=quest_type_id)
            serializer = QuestTypeSerializer(query)
            return Response(serializer.data)
        except QuestType.DoesNotExist:
            return Response({"error": "Quest_type does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = QuestTypeSerializer(data=request.data)
        if serializer.is_valid():
            new_quest_type = serializer.save()
            return Response({"quest_type_id": new_quest_type.quest_type_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, quest_type_id):
        try:
            updated_quest_type = QuestType.objects.get(quest_type_id=quest_type_id)
        except QuestType.DoesNotExist:
            return Response({"error": "Quest_type does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuestTypeSerializer(updated_quest_type, data=request.data)
        if serializer.is_valid():
            updated_quest_type = serializer.save()
            return Response({"quest_type_id": updated_quest_type.quest_type_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, quest_type_id):
        try:
            updated_quest_type = QuestType.objects.get(quest_type_id=quest_type_id)
        except QuestType.DoesNotExist:
            return Response({"error": "Quest_type does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuestTypeSerializer(updated_quest_type, data=request.data, partial=True)
        if serializer.is_valid():
            updated_quest_type = serializer.save()
            return Response({"quest_type_id": updated_quest_type.quest_type_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class QuestTypesEndPoint(APIView):

    def get(self, request):
        try:
            queryset = QuestType.objects.all()
            serializer = QuestTypeSerializer(queryset, many=True)
            return Response(serializer.data)
        except QuestType.DoesNotExist:
            return Response({"error": "QuestType does not exist"}, status=status.HTTP_404_NOT_FOUND)


class QuestEndPoint(APIView):

    def get(self, request, quest_id):
        try:
            query = Quest.objects.get(quest_id=quest_id)
            serializer = QuestSerializer(query)
            return Response(serializer.data)
        except Quest.DoesNotExist:
            return Response({"error": "Quest does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = QuestSerializer(data=request.data)
        if serializer.is_valid():
            new_quest = serializer.save()
            return Response({"quest_id": new_quest.quest_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, quest_id):
        try:
            updated_quest = Quest.objects.get(quest_id=quest_id)
        except Quest.DoesNotExist:
            return Response({"error": "Quest does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuestSerializer(updated_quest, data=request.data)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"quest_id": updated_quest.quest_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, quest_id):
        try:
            updated_quest = Quest.objects.get(quest_id=quest_id)
        except Quest.DoesNotExist:
            return Response({"error": "Quest does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuestSerializer(updated_quest, data=request.data, partial=True)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"quest_id": updated_quest.quest_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class QuestsEndPoint(APIView):

    def get(self, request):
        try:
            queryset = Quest.objects.all()
            serializer = QuestSerializer(queryset, many=True)
            return Response(serializer.data)
        except Quest.DoesNotExist:
            return Response({"error": "Quest does not exist"}, status=status.HTTP_404_NOT_FOUND)


class QuestReportEndPoint(APIView):

    def get(self, request, quest_report_id):
        try:
            query = QuestReport.objects.get(quest_report_id=quest_report_id)
            serializer = QuestReportSerializer(query)
            return Response(serializer.data)
        except QuestReport.DoesNotExist:
            return Response({"error": "Quest_report does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = QuestReportSerializer(data=request.data)
        if serializer.is_valid():
            new_quest = serializer.save()
            return Response({"quest_report_id": new_quest.quest_report_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, quest_report_id):
        try:
            updated_quest = QuestReport.objects.get(quest_report_id=quest_report_id)
        except QuestReport.DoesNotExist:
            return Response({"error": "Quest_report does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuestReportSerializer(updated_quest, data=request.data)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"quest_report_id": updated_quest.quest_report_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, quest_report_id):
        try:
            updated_quest = QuestReport.objects.get(quest_report_id=quest_report_id)
        except QuestReport.DoesNotExist:
            return Response({"error": "Quest_report does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuestReportSerializer(updated_quest, data=request.data, partial=True)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"quest_report_id": updated_quest.quest_report_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class QuestReportsEndPoint(APIView):

    def get(self, request):
        try:
            queryset = QuestReport.objects.all()
            serializer = QuestReportSerializer(queryset, many=True)
            return Response(serializer.data)
        except QuestReport.DoesNotExist:
            return Response({"error": "Quest_report does not exist"}, status=status.HTTP_404_NOT_FOUND)
