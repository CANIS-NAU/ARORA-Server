from django.urls import path

from . import views

urlpatterns = [
    path('dailytask/<int:daily_task_id>', views.DailyTaskEndPointByTaskId.as_view()),
    path('dailytask/<int:user_id>',views.DailyTaskEndPointByUserId.as_view()),
    path('dailytasks/complete', views.DailyTasksEndPointByComplete.as_view()),
]    
