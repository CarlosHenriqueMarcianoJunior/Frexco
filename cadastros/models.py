from asyncio.windows_events import NULL
from queue import Empty
from django.utils.crypto import get_random_string
import string
from unittest.util import _MAX_LENGTH
import django
from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
import random

random_pass = get_random_string(length=15)

class Cadastros(models.Model):
    users = models.CharField(primary_key=True, max_length= 70)
    password = models.CharField(max_length=15, default=random_pass) 
    nascimento = models.DateField()

