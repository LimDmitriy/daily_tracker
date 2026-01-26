from rest_framework import serializers


class HabitValidator:
    def __call__(self, value):
        is_enjoyable = value.get("is_enjoyable_habit")
        reward = value.get("reward")
        related_habit = value.get("related_habit")
        duration = value.get("duration")
        frequency = value.get("frequency")

        if is_enjoyable and (reward or related_habit):
            raise serializers.ValidationError(
                "Приятная привычка не может иметь вознаграждение или связанную привычку."
            )

        if reward and related_habit:
            raise serializers.ValidationError(
                "Нельзя указывать вознаграждение и связанную привычку одновременно."
            )

        if related_habit and not related_habit.is_enjoyable_habit:
            raise serializers.ValidationError(
                "Связанная привычка должна быть приятной."
            )

        if duration and duration.total_seconds() > 120:
            raise serializers.ValidationError(
                "Время выполнения не может превышать 120 секунд."
            )

        if frequency > 7:
            raise serializers.ValidationError(
                "Нельзя выполнять привычку реже, чем 1 раз в 7 дней."
            )
