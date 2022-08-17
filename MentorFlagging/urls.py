from django.urls import path
from . import views

urlpatterns = [
	path('MentorFlags/<int:mentor_id>' , views.AllMentorFlags.as_view() ),
	path('MenteeFlags/<int:mentee_id>', views.FlaggingEndpoints.as_view() ),
	path('Flags', views.FlaggingEndpoints.as_view() )
]
