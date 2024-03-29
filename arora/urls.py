"""arora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', include('UserInfos.urls')),
    path('', include('DailyTasks.urls')),
    path('', include('MoodReports.urls')),
  #  path('', include('DailyTasks.urls')),
    path('', include('Notifications.urls')),
    path('', include('ButterflyAtriums.urls')),
    path('', include('Butterflies.urls')),
    path('', include('Phrases.urls')),
    path('', include('BaselineReports.urls')),
    path('', include('UserInteractions.urls')),
    path('', include('Quests.urls')),
    path('', include('LocationReports.urls')),
    path('', include('SystemReports.urls')),
    path('', include('MentorChat.urls')),
    path('', include('AccessCodes.urls')),
    path('', include('MentorFlagging.urls')),
]
