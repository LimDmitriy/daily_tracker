from django.db import models

from users.models import User


class Habit(models.Model):
    PUBLIC_CHOISE = [
        ("public", "Публичный"),
        ("private", "Частный"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
    )
    place = models.CharField(
        max_length=255, verbose_name="Место", help_text="Укажите место"
    )
    time = models.TimeField(verbose_name="Время", help_text="Укажите время")
    action = models.CharField(
        max_length=255, verbose_name="Действие", help_text="Укажите действие"
    )
    is_enjoyable_habit = models.BooleanField(
        default=False,
        verbose_name="Признак приятной привычки",
        help_text="Укажите признак приятной привычки",
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="related_to",
        verbose_name="Связанная привычка",
        help_text="Укажите связанную привычку",
    )
    frequency = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Периодичность",
        help_text="Укажите периодичность привычки",
    )
    reward = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Вознаграждение",
        help_text="Укажите вознаграждение",
    )
    duration = models.DurationField(
        verbose_name="Время на выполнение", help_text="Укажите время на выполнение"
    )
    visibility = models.CharField(
        choices=PUBLIC_CHOISE,
        max_length=7,
        verbose_name="Признак публичности",
        help_text="Выберите признак публичности",
    )
