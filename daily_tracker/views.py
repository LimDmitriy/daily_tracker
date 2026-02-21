from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from daily_tracker.models import Habit
from daily_tracker.serializers import HabitSerializer
from daily_tracker.paginators import CustomPagination
from daily_tracker.permissions import IsOwner


class HabitCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return Habit.objects.filter(visibility="public")


class HabitRetrieveAPIView(RetrieveAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateAPIView(UpdateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitDestroyAPIView(DestroyAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
