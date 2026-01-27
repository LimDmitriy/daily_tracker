from django.contrib import admin

from daily_tracker.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    readonly_fields = ()
