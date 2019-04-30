from django.urls import path

from . import views

urlpatterns = [
    path('userinteraction/<int:user_interaction_id>', views.UserInteractionEndPoint.as_view()),
    path('userinteraction', views.UserInteractionEndPoint.as_view()),
    path('userinteractions', views.UserInteractionsEndPoint.as_view()),

    path('userinteractiontype/<int:user_interaction_type_id>', views.UserInteractionTypeEndPoint.as_view()),
    path('userinteractiontype', views.UserInteractionTypeEndPoint.as_view()),
    path('userinteractiontypes', views.UserInteractionTypesEndPoint.as_view()),
]
