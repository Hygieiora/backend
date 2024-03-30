from django.urls import reverse
from rest_framework.test import APITestCase
from accounts.views import *
import uuid


class AccountsUrlsTestCase(APITestCase):
    def test_user_list_url_resolves(self):
        view_name = "account-view"
        expected_url = reverse(view_name)

        self.assertEquals(expected_url, "/accounts/users/")

    def test_register_user_url_resolves(self):
        view_name = "auth-register"
        expected_url = reverse(view_name)

        self.assertEquals(expected_url, "/accounts/register/")

    def test_login_user_url_resolves(self):
        view_name = "auth-login"
        expected_url = reverse(view_name)

        self.assertEquals(expected_url, "/accounts/login/")


class UUIDViewTestCase(APITestCase):

    def test_user_detail_url_resolves(self):
        view_name = "account-detail"
        expected_url = reverse(view_name, args=[1])

        self.assertEquals(expected_url, f"/accounts/users/1/")