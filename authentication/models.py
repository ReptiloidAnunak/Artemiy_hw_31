import datetime
from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import ValidationError

from Avito30 import settings


def check_date(value: date):
    first_bd_year = datetime.datetime.now().year - 9
    if value.year > first_bd_year:
        raise ValidationError(f"Birth year can not be less {first_bd_year} and age less than 9")
    return True


def email_validator(email: str):
    not_allowed = settings.EMAIL_DOMAINS_NOT_ALLOWED
    if email.split("@")[1] in not_allowed:
        raise ValidationError(f"Addresses of domains {', '.join(not_allowed)} are not allowed")
    return True


class Location(models.Model):
    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    name = models.CharField(max_length=150)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    USER_ROLE = [("member", "Участник"),
                 ("moderator", "Модератор"),
                 ("admin", "Администратор")]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=USER_ROLE, default="member")
    location = models.ManyToManyField(Location)
    birth_date = models.DateField(null=True, validators=[check_date])
    email = models.EmailField(null=True, unique=True)

    def __str__(self):
        return self.username



