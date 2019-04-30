from django.urls import path

from . import views

urlpatterns = [
    path('baselinereport', views.BaselineReportEndPoint.as_view()),
    path('baselinereports', views.BaselineReportsEndPoint.as_view()),
    path('baselinereport/<int:baseline_report_id>', views.BaselineReportEndPoint.as_view()),
]
