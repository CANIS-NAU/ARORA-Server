from django.urls import path

from . import views

urlpatterns = [
    # path('', views.ButterflyList.as_view()),
    # path('<int:pk>/', views.ButterflyDetail.as_view()),
    path('userbutterfly/<int:user_butterfly_id>', views.UserButterflyEndPoint.as_view()),
    path('userbutterfly', views.UserButterflyEndPoint.as_view()),
    path('userbutterflies', views.UserButterfliesEndPoint.as_view()),

    path('butterfly/<int:butterfly_id>', views.ButterflyEndPoint.as_view()),
    path('butterfly', views.ButterflyEndPoint.as_view()),
    path('butterflies', views.ButterfliesEndPoint.as_view()),


    path('superfly/<int:superfly_id>', views.SuperflyEndPoint.as_view()),
    path('superfly', views.SuperflyEndPoint.as_view()),
    path('superflies', views.SuperfliesEndPoint.as_view()),
    path('superflies/<int:butterfly_atrium_id>', views.SuperfliesEndPointByButterflyAtriumId.as_view()),

    path('butterflytype/<int:butterfly_type_id>', views.ButterflyTypeEndPoint.as_view()),
    path('butterflytype', views.ButterflyTypeEndPoint.as_view()),
    path('butterflytypes', views.ButterflyTypesEndPoint.as_view()),

    # This is to like the profile picture butterfly 
    path('butterflylike/<int:butterfly_like_id>', views.ButterflyLikeEndPoint.as_view()),
    path('butterflylike', views.ButterflyLikeEndPoint.as_view()),
    path('butterflylikes', views.ButterflyLikesEndPoint.as_view()),


    path('butterflycomment/<int:butterfly_comment_id>', views.ButterflyCommentEndPoint.as_view()),
    path('butterflycomment', views.ButterflyCommentEndPoint.as_view()),
    path('butterflycomments', views.ButterflyCommentsEndPoint.as_view())
]
