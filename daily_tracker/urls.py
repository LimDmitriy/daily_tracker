from django.urls import path

from daily_tracker.apps import DailyTrackerConfig
from daily_tracker.views import (
    HabitCreateAPIView,
    HabitListAPIView,
    PublicHabitListAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
)

app_name = DailyTrackerConfig.name
urlpatterns = [
    path("habits/", HabitListAPIView.as_view()),
    path("habits/public/", PublicHabitListAPIView.as_view()),
    path("habits/create/", HabitCreateAPIView.as_view()),
    path("habits/<int:pk>/", HabitRetrieveAPIView.as_view()),
    path("habits/<int:pk>/update/", HabitUpdateAPIView.as_view()),
    path("habits/<int:pk>/delete/", HabitDestroyAPIView.as_view()),
]
