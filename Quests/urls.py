from django.urls import path

from . import views

urlpatterns = [
    # path('', views.QuestList.as_view()),
    # path('<int:pk>/', views.QuestDetail.as_view()),
    path('quest/<int:quest_id>', views.QuestEndPoint.as_view()),
    path('quest', views.QuestEndPoint.as_view()),
    path('quests', views.QuestsEndPoint.as_view()),

    path('questreport', views.QuestReportEndPoint.as_view()),
    path('questreport/<int:quest_report_id>', views.QuestReportEndPoint.as_view()),
    path('questreports', views.QuestReportsEndPoint.as_view()),

    path('queststatus', views.QuestStatusEndPoint.as_view()),
    path('queststatus/<int:quest_status_id>', views.QuestStatusEndPoint.as_view()),
    path('queststatuses', views.QuestStatusesEndPoint.as_view()),

    path('questtype', views.QuestTypeEndPoint.as_view()),
    path('questtype/<int:quest_type_id>', views.QuestTypeEndPoint.as_view()),
    path('questtypes', views.QuestTypesEndPoint.as_view()),

]
