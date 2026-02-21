import pytest
from rest_framework.test import APIClient

from users.models import User


@pytest.mark.django_db
def test_habit_list_authenticated():
    user = User.objects.create(email="u@test.com")
    user.set_password("1234")
    user.save()

    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get("/daily_tracker/habits/")

    assert response.status_code == 200
