import pytest
from rest_framework.serializers import ValidationError
from daily_tracker.validators import HabitValidator


def test_enjoyable_habit_with_reward_error():
    validator = HabitValidator()

    data = {
        "is_enjoyable_habit": True,
        "reward": "Кофе",
        "related_habit": None,
    }

    with pytest.raises(ValidationError):
        validator(data)
