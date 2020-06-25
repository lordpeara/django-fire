from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import (
    PBKDF2PasswordHasher, PBKDF2SHA1PasswordHasher,
    make_password,
)
from django.core.management import CommandError, call_command
from django.test import TestCase

from django_fire.hashers import FIRED_PASSWORD_PREFIX

UserModel = get_user_model()


class TestCommand(TestCase):
    def setUp(self):
        # user with sha256 hasher
        self.user = UserModel.objects.create_user('test-user-1')
        self.user.password = make_password(
            'password', hasher=PBKDF2PasswordHasher.algorithm,
        )
        self.user.save()

        # user with sha1 hasher
        self.algorithm = PBKDF2SHA1PasswordHasher.algorithm
        user = UserModel.objects.create_user('test-user-2')
        user.password = make_password('password', hasher=self.algorithm)
        user.save()

    def test_command_without_any_argument(self):
        with self.assertRaises(CommandError):
            call_command('firepassword')

    def test_command_for_all_users(self):
        call_command('firepassword', '--all')
        fired_count = UserModel.objects.filter(
            password__startswith=FIRED_PASSWORD_PREFIX
        ).count()
        self.assertEqual(fired_count, 2)

    def test_command_by_specific_users(self):
        call_command('firepassword', '--users', self.user.pk)
        user = UserModel.objects.get(
            password__startswith=FIRED_PASSWORD_PREFIX
        )
        self.assertEqual(user.pk, self.user.pk)

    def test_command_by_specific_hashers(self):
        pass
