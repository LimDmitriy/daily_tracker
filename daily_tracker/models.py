from django.db import models
from users.models import User


class Habit(models.Model):
    PUBLIC_CHOICES = [
        ("public", "Публичный"),
        ("private", "Частный"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    place = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)

    is_enjoyable_habit = models.BooleanField(default=False)

    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="related_to",
    )

    frequency = models.PositiveSmallIntegerField(default=1)
    reward = models.CharField(max_length=255, blank=True)
    duration = models.DurationField()

    visibility = models.CharField(
        max_length=7,
        choices=PUBLIC_CHOICES,
        default="private",
    )
    last_sent = models.DateField(
        null=True, blank=True, verbose_name="Дата последнего напоминания"
    )

    def __str__(self):
        return f"{self.action} ({self.user})"
