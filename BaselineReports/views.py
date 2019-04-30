from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BaselineReport
from .serializers import BaselineReportSerializer


class BaselineReportList(generics.ListAPIView):
    queryset = BaselineReport.objects.all()
    serializer_class = BaselineReportSerializer


class BaselineReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BaselineReport.objects.all()
    serializer_class = BaselineReportSerializer
    

class BaselineReportEndPoint(APIView):

    def get(self, request, baseline_report_id):
        try:
            query = BaselineReport.objects.get(baseline_report_id=baseline_report_id)
            serializer = BaselineReportSerializer(query)
            return Response(serializer.data)
        except BaselineReport.DoesNotExist:
            return Response({"error": "BaselineReport does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = BaselineReportSerializer(data=request.data)
        if serializer.is_valid():
            new_quest = serializer.save()
            return Response({"baseline_report_id": new_quest.baseline_report_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, baseline_report_id):
        try:
            updated_quest = BaselineReport.objects.get(baseline_report_id=baseline_report_id)
        except BaselineReport.DoesNotExist:
            return Response({"error": "BaselineReport does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BaselineReportSerializer(updated_quest, data=request.data)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"baseline_report_id": updated_quest.baseline_report_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, baseline_report_id):
        try:
            updated_quest = BaselineReport.objects.get(baseline_report_id=baseline_report_id)
        except BaselineReport.DoesNotExist:
            return Response({"error": "BaselineReport does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BaselineReportSerializer(updated_quest, data=request.data, partial=True)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"baseline_report_id": updated_quest.baseline_report_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class BaselineReportsEndPoint(APIView):

    def get(self, request):
        try:
            queryset = BaselineReport.objects.all()
            serializer = BaselineReportSerializer(queryset, many=True)
            return Response(serializer.data)
        except BaselineReport.DoesNotExist:
            return Response({"error": "BaselineReport does not exist"}, status=status.HTTP_404_NOT_FOUND)
