import factory
from ads.models import Ad, Category, Selection
from authentication.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "12345"


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "category_test"
    slug = factory.Faker("color")


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "test_ad"
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    price = 1
    description = "test"


class SelectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Selection

    owner = factory.SubFactory(UserFactory)
    name = "test_selection"
    items = factory.SubFactory(AdFactory)
