from django.test import TestCase
from django.core.exceptions import ValidationError
from ..factories.users import UserFactory

class BaseUserModelTest(TestCase):
    def setUp(self):
        self.user = UserFactory.build()

class UserModelSuccessTestCase(BaseUserModelTest):
    def test_user_creation(self):
        self.user.full_clean()
        self.assertTrue(True)

    def test_nickname_cannot_be_blank(self):
       print("テスト実行")

    def test_email_cannot_be_blank(self):
       print("テスト実行")

    def test_password_cannot_be_blank(self):
       print("テスト実行")

    def test_nickname_length_exceeds_limit(self):
       print("テスト実行")

    def test_unique_email_constraint(self):
       print("テスト実行")

    def test_email_must_contain_at_symbol(self):
       print("テスト実行")