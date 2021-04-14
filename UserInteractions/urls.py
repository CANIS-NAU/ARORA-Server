from django.urls import path

from . import views

urlpatterns = [
    path('userinteraction/<int:user_interaction_id>', views.UserInteractionEndPoint.as_view()),
    path('userinteraction', views.UserInteractionEndPoint.as_view()),
    path('userinteractions', views.UserInteractionsEndPoint.as_view()),

    path('userinteractiontype/<int:user_interaction_type_id>', views.UserInteractionTypeEndPoint.as_view()),
    path('userinteractiontype', views.UserInteractionTypeEndPoint.as_view()),
    path('userinteractiontypes', views.UserInteractionTypesEndPoint.as_view()),

    # Paths for getting UserInteraction records by sender or by receiver
    path('userinteraction/<int:quest_record_id>', views.UserInteractionsEndPointByQuestReportId.as_view()),
    path('userinteraction/<int:initiator_user_id>', views.UserInteractionsEndPointByInitiator.as_view()),
    path('interactioninitnotifs/<int:initiator_user_id>', views.UserInteractionsEndPointByInitiatorAndNotifType.as_view()),
    path('userinteraction/<int:receiver_user_id>', views.UserInteractionsEndPointByReceiver.as_view()),

    # Paths to view, join, and delete a user session
    #path('superflysession/<int:session_id>', views.SuperflySessionEndpoint.as_view()),
    path('superflysession', views.SuperflySessionEndpoint.as_view())

]    
