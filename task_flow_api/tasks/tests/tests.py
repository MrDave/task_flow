from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

import pytest
import httpx
from pytest_django.fixtures import django_db_setup

USERS = [
    {
        "username": "JakeTheDog",
        "email": "jakethedog@example.com",
        "password": "good_boi_123",
    },
    {
        "username": "MothMan",
        "email": "mothman@example.com",
        "password": "sharethelamp1",
    }
]

TASKS = [
    {
        "name": "Be a brick",
        "is_completed": True,
        "owner": "JakeTheDog",
    },
    {
        "name": "Marry Lady Rainicorn",
        "owner": "JakeTheDog",
    },
    {
        "name": "Lick a lamp",
        "is_completed": False,
        "owner": "MothMan",
    },
    {
        "name": "Fly around",
        "is_completed": True,
        "owner": "MothMan",
    }
]

URLS = {
    "token": "http://localhost:8000/api/token/",
    "tasks": "http://127.0.0.1:8000/api/tasks/",
    "task_detail": "http://127.0.0.1:8000/api/token/1/",
}

@pytest.mark.django_db
class TestUsers(TestCase):

    def test_create_users(self):
        for user in USERS:
            User.objects.create_user(**user)
        assert User.objects.all()
    # def test_create_task(self):
    #     username, email, password = USERS[0]
    #     user = User.objects.create_user(username=username, email=email, password=password)
    #     assert user.username == username
    #
    #     token_response = httpx.post(URLS["token"], json={"username": username, "password": password})
    #     token_response.raise_for_status()
    #     #
    #     # access_token = token_response.json()["access"]
    #     #
