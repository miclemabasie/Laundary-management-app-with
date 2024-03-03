from django.test import SimpleTestCase
from django.urls import resolve, reverse
from apps.subscriptions.views import create_subscription, list_subscriptions, user_subscription_details

class TestSubscriptionUrls(SimpleTestCase):

    def test_create_subscription_url_resolves(self):
        """Test that the create subscription URL resolves to the correct view."""
        url = reverse("subscriptions:create-subscription")
        self.assertEqual(resolve(url).func, create_subscription)

    def test_list_subscription_url_resolves(self):
        """Test that the list subscription URL resolves to the correct view."""
        url = reverse("subscriptions:list-subscription")
        self.assertEqual(resolve(url).func, list_subscriptions)

    def test_user_subscription_detail_url_resolves(self):
        """Test that the user subscription detail URL resolves to the correct view."""
        url = reverse("subscriptions:get-user-subscription")
        self.assertEqual(resolve(url).func, user_subscription_details)
