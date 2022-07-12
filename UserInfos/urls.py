from django.conf.urls import url
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from . import views

urlpatterns = [
    # path('test', views.UserInfoList.as_view()),
    # path('<int:pk>/', views.UserInfoDetail.as_view()),
    # path('user_test', views.UserList.as_view()),

    # url(r'user/(?P<user_id>\d+)', views.UserInfos.as_view()),
    path('userinfo/<int:user_id>', views.UserInfos.as_view()),
    path('userinfo', views.UserInfos.as_view()),
    path('userinfos', views.AllUserInfos.as_view()),
    path('nearbyusers/<int:user_id>', views.NearByUser.as_view()),
    path('unassignedmentees/<int:user_id>' , views.UnassignedMenteeList.as_view()),
    path('assignedmentees/<int:mentor_id>' , views.MentorAssignedList.as_view()),
    path('changementor/<int:user_id>' , views.ChangeAssignedMentor.as_view()),
    url('api-token-auth', obtain_jwt_token),
    url('api-token-refresh', refresh_jwt_token),
    url('api-token-verify', verify_jwt_token)
]
