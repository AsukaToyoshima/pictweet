from django.test import TestCase
from django.test.utils import override_settings
from django.core.exceptions import ValidationError
from django.conf import settings
from ..factories.tweets import TweetFactory
from ..factories.users import UserFactory
import os
import shutil

class BaseUserModelTest(TestCase):
    def setUp(self):
        self.user = UserFactory.create()
        self.tweet = TweetFactory.build(user=self.user)

class TweetModelSuccessTestCase(BaseUserModelTest):
    def test_tweet_creation(self):
        self.tweet.full_clean()

    def test_tweet_with_text_only(self):
        self.tweet.image = None
        self.tweet.full_clean()

class TweetModelFailureTestCase(BaseUserModelTest):
    def test_tweet_without_text(self):
       print("テスト実行")

    def test_tweet_without_user(self):
       print("テスト実行")
