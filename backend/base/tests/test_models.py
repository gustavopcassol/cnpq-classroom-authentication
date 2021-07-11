from datetime import timedelta
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase

from base.exceptions import InvalidTemporaryTokenError
from base.models import TemporaryToken

User = get_user_model()


class TemporaryTokenCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="user")
        self.temporary_token = TemporaryToken.objects.create(user=user)

    @patch("django.utils.timezone.now")
    def test_has_not_expired(self, mock_now):
        mock_now.return_value = self.temporary_token.created

        self.assertIsNone(self.temporary_token.check_if_valid())

    @patch("django.utils.timezone.now")
    def test_has_expired(self, mock_now):
        mock_now.return_value = self.temporary_token.created + timedelta(
            minutes=5, milliseconds=1
        )

        with self.assertRaisesMessage(InvalidTemporaryTokenError, "expired token"):
            self.temporary_token.check_if_valid()