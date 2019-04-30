from django.urls import path

from . import views

urlpatterns = [
    # path('phrases', views.PhraseList.as_view()),
    # path('phrases/<int:phrase_id>/', views.PhraseDetail.as_view()),
    path('phrase/<int:phrase_id>', views.PhraseEndPoint.as_view()),
    path('phrase', views.PhraseEndPoint.as_view()),
    path('phrases', views.PhrasesEndPoint.as_view()),
]
