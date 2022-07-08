from django.urls import path
from . import views

urlpatterns = [
	path('AccessCodes' , views.AllAccessCodes.as_view()),
	path('AccessCode/<str:access_code>' , views.AccessCodeEndpoints.as_view()),
	path('AccessCode' , views.AccessCodeEndpoints.as_view())
]
