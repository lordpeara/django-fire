from django.contrib.auth.hashers import UNUSABLE_PASSWORD_PREFIX
from django.test import TestCase

from django_fire.hashers import (
    FIRED_PASSWORD_PREFIX,
    is_password_fired, make_fired_password,
)


class TestHashers(TestCase):
    def test_is_password_fired(self):
        # unusable password made by django_fire should be True
        self.assertTrue(is_password_fired(FIRED_PASSWORD_PREFIX))
        # unusable password not made by django_fire should be False
        self.assertFalse(is_password_fired(UNUSABLE_PASSWORD_PREFIX))

    def test_make_fired_password(self):
        fired_password = make_fired_password()
        # fired password should be UNUSABLE PASSWORD as django
        self.assertTrue(fired_password.startswith(UNUSABLE_PASSWORD_PREFIX))
        # fired password should be FIRED PASSWORD as django_fire
        self.assertTrue(fired_password.startswith(FIRED_PASSWORD_PREFIX))
        # django_fire should be able to check fired-password
        self.assertTrue(is_password_fired(fired_password))
