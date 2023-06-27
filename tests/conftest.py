from pytest_factoryboy import register
from tests.factories import CategoryFactory, UserFactory, AdFactory, SelectionFactory

pytest_plugins = "tests.fixtures"

register(CategoryFactory)
register(UserFactory)
register(AdFactory)
register(SelectionFactory)

