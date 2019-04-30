from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SystemReport
from .serializers import SystemReportSerializer


class SystemReportList(generics.ListAPIView):
    queryset = SystemReport.objects.all()
    serializer_class = SystemReportSerializer


class SystemReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SystemReport.objects.all()
    serializer_class = SystemReportSerializer


class SystemReportEndPoint(APIView):

    def get(self, request, system_report_id):
        try:
            query = SystemReport.objects.get(system_report_id=system_report_id)
            serializer = SystemReportSerializer(query)
            return Response(serializer.data)
        except SystemReport.DoesNotExist:
            return Response({"error": "SystemReport does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = SystemReportSerializer(data=request.data)
        if serializer.is_valid():
            new_quest = serializer.save()
            return Response({"system_report_id": new_quest.system_report_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, system_report_id):
        try:
            updated_quest = SystemReport.objects.get(system_report_id=system_report_id)
        except SystemReport.DoesNotExist:
            return Response({"error": "SystemReport does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SystemReportSerializer(updated_quest, data=request.data)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"system_report_id": updated_quest.system_report_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, system_report_id):
        try:
            updated_quest = SystemReport.objects.get(system_report_id=system_report_id)
        except SystemReport.DoesNotExist:
            return Response({"error": "SystemReport does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SystemReportSerializer(updated_quest, data=request.data, partial=True)
        if serializer.is_valid():
            updated_quest = serializer.save()
            return Response({"system_report_id": updated_quest.system_report_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SystemReportsEndPoint(APIView):

    def get(self, request):
        try:
            queryset = SystemReport.objects.all()
            serializer = SystemReportSerializer(queryset, many=True)
            return Response(serializer.data)
        except SystemReport.DoesNotExist:
            return Response({"error": "SystemReport does not exist"}, status=status.HTTP_404_NOT_FOUND)
