from django.urls import path

from . import views

urlpatterns = [
    # path('', views.MoodReportList.as_view()),
    # path('<int:pk>/', views.MoodReportDetail.as_view()),
    path('moodreport/<int:mood_report_id>', views.MoodReportEndPoint.as_view()),
    path('moodreports', views.MoodReportsEndPoint.as_view()),
    path('moodreport', views.MoodReportEndPoint.as_view()),
    path('moodtype', views.MoodTypeEndPoint.as_view()),
    path('moodtype/<int:mood_type_id>', views.MoodTypeEndPoint.as_view()),
    path('moodtypes', views.MoodTypesEndPoint.as_view()),
]
