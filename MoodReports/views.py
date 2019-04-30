from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

# mood_type_set = list(MoodType.objects.values_list('MoodTypeId', flat=True))


mood_type_set = []   # This is for initialize


class MoodReportList(generics.ListAPIView):
    queryset = MoodReport.objects.all()
    serializer_class = MoodReportSerializer


class MoodReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoodReport.objects.all()
    serializer_class = MoodReportSerializer


class MoodReportEndPoint(APIView):

    def get(self, request, mood_report_id):
        try:
            query = MoodReport.objects.get(mood_report_id=mood_report_id)
            serializer = MoodReportSerializer(query)
            return Response(serializer.data)
        except MoodReport.DoesNotExist:
            return Response({"error": "Mood_report does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = MoodReportSerializer(data=request.data)
        if serializer.is_valid():
            new_mood_report = serializer.save()
            return Response({"mood_report_id": new_mood_report.mood_report_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, mood_report_id):
        try:
            updated_mood_report = MoodReport.objects.get(mood_report_id=mood_report_id)
        except MoodReport.DoesNotExist:
            return Response({"error": "Mood_report does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MoodReportSerializer(updated_mood_report, data=request.data)
        if serializer.is_valid():
            updated_mood_report = serializer.save()
            return Response({"mood_report_id": updated_mood_report.mood_report_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, mood_report_id):
        try:
            updated_mood_report = MoodReport.objects.get(mood_report_id=mood_report_id)
        except MoodReport.DoesNotExist:
            return Response({"error": "Mood_report does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MoodReportSerializer(updated_mood_report, data=request.data, partial=True)
        if serializer.is_valid():
            updated_mood_report = serializer.save()
            return Response({"mood_report_id": updated_mood_report.mood_report_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class MoodReportsEndPoint(APIView):

    def get(self, request):
        try:
            queryset = MoodReport.objects.all()
            serializer = MoodReportSerializer(queryset, many=True)
            return Response(serializer.data)
        except MoodReport.DoesNotExist:
            return Response({"error": "Mood_report does not exist"}, status=status.HTTP_404_NOT_FOUND)


class MoodTypeEndPoint(APIView):

    def get(self, request, mood_type_id):
        try:
            query = MoodType.objects.get(mood_type_id=mood_type_id)
            serializer = MoodTypeSerializer(query)
            return Response(serializer.data)
        except MoodType.DoesNotExist:
            return Response({"error": "Mood_type does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = MoodTypeSerializer(data=request.data)
        if serializer.is_valid():
            new_mood_type = serializer.save()
            return Response({"mood_type_id": new_mood_type.mood_type_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, mood_type_id):
        try:
            updated_mood_type = MoodType.objects.get(mood_type_id=mood_type_id)
        except MoodType.DoesNotExist:
            return Response({"error": "Mood_type does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MoodTypeSerializer(updated_mood_type, data=request.data)
        if serializer.is_valid():
            updated_mood_type = serializer.save()
            return Response({"mood_type_id": updated_mood_type.mood_type_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, mood_type_id):
        try:
            updated_mood_type = MoodType.objects.get(mood_type_id=mood_type_id)
        except MoodType.DoesNotExist:
            return Response({"error": "Mood_type does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MoodTypeSerializer(updated_mood_type, data=request.data, partial=True)
        if serializer.is_valid():
            updated_mood_type = serializer.save()
            return Response({"mood_type_id": updated_mood_type.mood_type_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class MoodTypesEndPoint(APIView):

    def get(self, request):
        try:
            queryset = MoodType.objects.all()
            serializer = MoodTypeSerializer(queryset, many=True)
            return Response(serializer.data)
        except MoodType.DoesNotExist:
            return Response({"error": "Mood_type does not exist"}, status=status.HTTP_404_NOT_FOUND)