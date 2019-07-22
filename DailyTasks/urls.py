from django.urls import path

from . import views

urlpatterns = [
    path('dailytask/<int:daily_task_id>', views.DailyTaskEndPoint.as_view()),
    path('dailytask/user/<int:user_id>',views.DailyTaskEndPointByUserId.as_view()),
    path('dailytasks/', views.DailyTasksEndPoint.as_view()),
    path('dailytasks/complete', views.DailyTasksEndPointByComplete.as_view()),
]    
