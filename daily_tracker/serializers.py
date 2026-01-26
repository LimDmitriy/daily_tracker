from rest_framework.serializers import ModelSerializer
from daily_tracker.models import Habit
from daily_tracker.validators import HabitValidator


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [HabitValidator()]
