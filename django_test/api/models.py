import random
import string

from django.db import models


def generate_api_key() -> str:
    alphabet = string.ascii_letters
    return ''.join(random.choice(alphabet) for _ in range(32))


class App(models.Model):
    name = models.CharField(max_length=128)
    api_key = models.CharField(max_length=32, unique=True, default=generate_api_key)
