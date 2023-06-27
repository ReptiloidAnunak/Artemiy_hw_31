from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from authentication.models import User


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    name = models.CharField(max_length=100)
    slug = models.CharField(validators=[MinLengthValidator(5)], max_length=10, unique=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Ad(models.Model):
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["name"]

    name = models.CharField(validators=[MinLengthValidator(10)], max_length=500, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    description = models.CharField(max_length=4000, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to="./images", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Selection(models.Model):
    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=40)
    items = models.ManyToManyField(Ad)

    def __str__(self):
        return f"Подборка {self.owner.first_name}"