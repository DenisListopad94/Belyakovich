from django.test import TestCase
from base.models import User


class UserModelTest(TestCase):

    def setUp(self):
        self.user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'age': 30,
            'locale': 'en_US',
            'sex': 'm'
        }
        self.user = User.objects.create(**self.user_data)

    def test_user_creation(self):
        user = self.user
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.email, 'john.doe@example.com')
        self.assertEqual(user.age, 30)
        self.assertEqual(user.locale, 'en_US')
        self.assertEqual(user.sex, 'm')

    def test_user_str_method(self):
        user = self.user
        self.assertEqual(str(user), 'Doe')

    # email уникальный
    def test_user_email_uniqueness(self):
        with self.assertRaises(Exception):
            User.objects.create(
                first_name='Jane',
                last_name='Smith',
                email='john.doe@example.com',  # Этот email уже существует
                age=25,
                locale='en_GB',
                sex='f'
            )

    # возраст положительный
    def test_user_age_validation(self):
        with self.assertRaises(ValueError):
            User.objects.create(
                first_name='Alice',
                last_name='Johnson',
                email='alice.johnson@example.com',
                age=-5,  # Невалидный возраст
                locale='fr_FR',
                sex='f'
            )

    # sex - правильные
    def test_user_sex_choices(self):

        user_male = User.objects.create(
            first_name='Tom',
            last_name='Smith',
            email='tom.smith@example.com',
            age=40,
            locale='en_US',
            sex='m'
        )
        user_female = User.objects.create(
            first_name='Mary',
            last_name='Johnson',
            email='mary.johnson@example.com',
            age=35,
            locale='en_GB',
            sex='f'
        )
        self.assertEqual(user_male.sex, 'M')
        self.assertEqual(user_female.sex, 'F')
        # Проверим, что ошибка возникает при попытке установить некорректное значение
        with self.assertRaises(ValueError):
            User.objects.create(
                first_name='Invalid',
                last_name='User',
                email='invalid.user@example.com',
                age=29,
                locale='de_DE',
                sex='x'  # Некорректное значение для sex
            )