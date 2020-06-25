import mock
from django.contrib.auth import get_user_model
from django.contrib.messages.api import get_messages
from django.contrib.messages.constants import DEFAULT_LEVELS
from django.contrib.messages.storage.base import Message
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import TestCase
from django.test.client import RequestFactory
from django.utils.translation import gettext_lazy as _

from django_fire.backends import FiredPasswordBackend
from django_fire.exceptions import FiredPassword
from django_fire.hashers import make_fired_password

UserModel = get_user_model()


class TestBackend(TestCase):
    backend = FiredPasswordBackend()

    def setUp(self):
        # user with fired password
        self.user = UserModel.objects.create_user(
            username='test-user', email=None, password='test-password',
        )
        self.user.password = make_fired_password()
        self.user.save()

        # patch mock request to use session & messages
        self.request = RequestFactory().get('')
        self.request.session = 'session'
        self.request._messages = FallbackStorage(self.request)

    def test_backend_for_normal_user(self):
        # Given normal (not fired) password
        self.user.set_password('normal_password')
        self.user.save()

        # nothing happend
        username = getattr(self.user, UserModel.USERNAME_FIELD)
        self.backend.authenticate(self.request, username=username)

    def test_backend_when_user_is_fired(self):
        # Given user whose password is fired
        username = getattr(self.user, UserModel.USERNAME_FIELD)

        # Custom Exception (FiredPassword) should be raised.
        with self.assertRaises(FiredPassword):
            self.backend.authenticate(self.request, username=username)

        # Message for fired password should be included.
        messages = get_messages(self.request)
        self.assertEqual(len(messages), 1)
        actual_message = list(messages)[0]
        expected_message = Message(
            level=DEFAULT_LEVELS['ERROR'],
            message=_('Your password is fired. please reset your password '
                      'through password reset request.'),
        )
        self.assertEqual(actual_message, expected_message)

    @mock.patch('django.contrib.auth.models.User')
    def test_backend_when_user_does_not_exist(self, User):
        # Given no user for given username
        User.USERNAME_FIELD = 'custom_username_field'
        username = 'this-user-does-not-exist'
        # should be None
        self.assertIsNone(self.backend.authenticate(self.request, **{'custom_username_username':username}))
