from django.urls import path

from . import views

urlpatterns = [
    path('locationreport/<int:location_report_id>', views.LocationReportEndPoint.as_view()),
    path('locationreport', views.LocationReportEndPoint.as_view()),
    path('locationreports', views.LocationReportsEndPoint.as_view()),
]
