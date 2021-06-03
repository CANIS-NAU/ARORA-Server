from django.urls import path

from . import views

urlpatterns = [
    path('usersuperfly/', views.UserSuperflyEndPoint.as_view()),
    path('usersuperfly/<int:user_id>', views.UserSuperflyEndPoint.as_view()),

]
