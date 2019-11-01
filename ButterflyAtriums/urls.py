from django.urls import path

from . import views

urlpatterns = [
    path('butterflyatrium/<int:butterfly_atrium_id>', views.ButterflyAtriumEndPoint.as_view()),
    path('butterflyatrium/<int:butterfly_atrium_user_id>', views.ButterflyAtriumEndPointByUserId.as_view()),

]
