from django.urls import path

from . import views

urlpatterns = [
    # path('systemreports', views.SystemReportList.as_view()),
    # path('systemreport/<int:pk>/', views.SystemReportDetail.as_view()),
    path('systemreport', views.SystemReportEndPoint.as_view()),
    path('systemreport/<int:system_report_id>', views.SystemReportEndPoint.as_view()),
    path('systemreports', views.SystemReportsEndPoint.as_view()),
]
