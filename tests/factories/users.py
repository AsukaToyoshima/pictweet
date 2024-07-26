import factory
from django.conf import settings
import faker

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    nickname = factory.LazyAttribute(lambda obj: faker.Faker().first_name()[:10])
    email = factory.Faker('email')
    password = factory.Faker('password')