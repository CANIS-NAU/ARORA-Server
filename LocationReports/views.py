from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import LocationReport
from .serializers import LocationReportSerializer


class LocationReportList(generics.ListAPIView):
    queryset = LocationReport.objects.all()
    serializer_class = LocationReportSerializer


class LocationReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LocationReport.objects.all()
    serializer_class = LocationReportSerializer


class LocationReportEndPoint(APIView):

    def post(self, request):
        try:
            location_report_lat = request.data['latitude']
            location_report_long = request.data['longitude']
        except KeyError:
            return Response({"error": "Wrong Json Format"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_id = request.user
        except ValueError:
            return Response({"error": "User not Found"}, status=status.HTTP_404_NOT_FOUND)

        new_location_report = LocationReport.objects.create(LocationReportLat=location_report_lat,
                                                            LocationReportLong=location_report_long,
                                                            UserId=user_id)
        return Response({"location_report_id": new_location_report.LocationReportId}, status=status.HTTP_200_OK)


class LocationReportEndPoint(APIView):

    def get(self, request, location_report_id):
        try:
            query = LocationReport.objects.get(location_report_id=location_report_id)
            serializer = LocationReportSerializer(query)
            return Response(serializer.data)
        except LocationReport.DoesNotExist:
            return Response({"error": "Location_report does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = LocationReportSerializer(data=request.data)
        if serializer.is_valid():
            new_location_report = serializer.save()
            return Response({"location_report_id": new_location_report.location_report_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, location_report_id):
        try:
            updated_location_report = LocationReport.objects.get(location_report_id=location_report_id)
        except LocationReport.DoesNotExist:
            return Response({"error": "Location_report does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = LocationReportSerializer(updated_location_report, data=request.data)
        if serializer.is_valid():
            updated_location_report = serializer.save()
            return Response({"location_report_id": updated_location_report.location_report_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, location_report_id):
        try:
            updated_location_report = LocationReport.objects.get(location_report_id=location_report_id)
        except LocationReport.DoesNotExist:
            return Response({"error": "Location_report does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = LocationReportSerializer(updated_location_report, data=request.data, partial=True)
        if serializer.is_valid():
            updated_location_report = serializer.save()
            return Response({"location_report_id": updated_location_report.location_report_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LocationReportsEndPoint(APIView):

    def get(self, request):
        try:
            queryset = LocationReport.objects.all()
            serializer = LocationReportSerializer(queryset, many=True)
            return Response(serializer.data)
        except LocationReport.DoesNotExist:
            return Response({"error": "Location_report does not exist"}, status=status.HTTP_404_NOT_FOUND)


