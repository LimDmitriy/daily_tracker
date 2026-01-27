from celery import shared_task
from django.utils import timezone
from datetime import timedelta

from daily_tracker.models import Habit
from daily_tracker.services import send_telegram_message


@shared_task
def send_habit_reminders():
    now = timezone.localtime()

    habits = Habit.objects.filter(
        time__hour=now.hour,
        time__minute=now.minute,
        user__telegram_chat_id__isnull=False,
        visibility=True,
    )

    for habit in habits:
        if habit.last_sent:
            next_date = habit.last_sent + timedelta(days=habit.frequency)
            if now.date() < next_date:
                continue

        send_telegram_message(
            habit.user.telegram_chat_id,
            f"⏰ Напоминание!\n" f"Привычка: {habit.action}\n" f"Место: {habit.place}",
        )

        habit.last_sent = now.date()
        habit.save(update_fields=["last_sent"])
