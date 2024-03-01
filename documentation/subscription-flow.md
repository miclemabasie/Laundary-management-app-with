# Subscription Feature Documentation

## Overview

The subscription feature allows users to choose from different subscription plans, each offering varying levels of access and additional perks. This documentation provides details on the implementation, usage, and considerations for the subscription feature.

## Table of Contents

- [Implementation Details](#implementation-details)
- [Usage](#usage)
- [Examples](#examples)
- [Considerations](#considerations)
- [Future Enhancements](#future-enhancements)

## Implementation Details

### Code Structure

The subscription feature is implemented using Django models, views, and serializers.

- `User` model: Represents different subscription plans with fields for name, price, features, etc.
- `Subscription` model: Represents the user's subscription with a foreign key to `User`.
- `SubscriptionCreateSerailizer`: Serializes subscription data for API interactions (Used only for creating Subscription instances in the system).
- `SubscriptionListSerializer`: Handles data serialization for listing out subscriptions through the API.
- `create_subscription`: Handles API endpoints for subscribing to a subscription plan.
- `list_subscriptions`: Handles API endpoints for listing out all subscription plans.
- `user_subscription_details`: Handles API endpoints for retrieving all subscription information about the currently logged-in user.

### Data Models

#### SubscriptionPlan Model

```python
class Subscription(TimeStampedUUIDModel):

    PLAN_CHOICES = [
        ("basic", "Basic"),
        ("standard", "Standard"),
        ("premium", "Premium"),
    ]

    shop_owner = models.ForeignKey(
        User, related_name="subscriptions", on_delete=models.SET_NULL, blank=True, null=True
    )
    plan_type = models.CharField(
        verbose_name=_("Plan Type"), max_length=20, choices=PLAN_CHOICES
    )
    transaction_id = models.CharField(
        verbose_name=_("Transaction_id"),
        max_length=20,
        unique=True,
        blank=True,
        null=True,
    )

    # Core features

    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    # Basic Plan Features
    basic_order_tracking = models.BooleanField(default=True)
    basic_subscription_plans = models.BooleanField(default=True)
    basic_customer_support = models.BooleanField(default=True)
    basic_limited_image_uploads = models.BooleanField(default=True)
    basic_basic_email_campaigns = models.BooleanField(default=True)
    basic_gallery_and_portfolio = models.BooleanField(default=True)
    basic_limited_access_tutorials_guides = models.BooleanField(default=True)

    # Standard Plan Features
    standard_order_tracking = models.BooleanField(default=False)
    standard_customer_support = models.BooleanField(default=False)
    standard_enhanced_image_uploads = models.BooleanField(default=False)
    standard_basic_email_campaigns = models.BooleanField(default=False)
    standard_portfolio_showcase = models.BooleanField(default=False)
    standard_standard_industry_resources = models.BooleanField(default=False)
    standard_webinars_training_sessions = models.BooleanField(default=False)

    # Premium Plan Features
    premium_order_tracking = models.BooleanField(default=False)
    premium_customer_support = models.BooleanField(default=False)
    premium_ai_powered_insights = models.BooleanField(default=False)
    premium_integration_with_ai_tools = models.BooleanField(default=False)
    premium_custom_reports = models.BooleanField(default=False)
    premium_marketing_campaigns = models.BooleanField(default=False)
    premium_gallery_and_portfolio = models.BooleanField(default=False)
    premium_training_and_resources = models.BooleanField(default=False)

    def save(self, *a, **kw) -> None:
        # Auto-fill in the transaction ID
        self.transaction_id = str(uuid.uuid4())[-17:]
        # Calculate and save prices based on plan choice
        self.start_date = timezone.now()
        self.end_date = self.start_date + timedelta(365)
        if self.plan_type == "basic":
            self.price = 0.0
        elif self.plan_type == "standard":
            # Standard Plan Features
            self.standard_order_tracking = True
            self.standard_customer_support = True
            self.standard_enhanced_image_uploads = True
            self.standard_basic_email_campaigns = True
            self.standard_portfolio_showcase = True
            self.standard_standard_industry_resources = True
            self.standard_webinars_training_sessions = True
            self.price = 10.0
        elif self.plan_type == "premium":
            # standard plan features
            self.standard_order_tracking = True
            self.standard_customer_support = True
            self.standard_enhanced_image_uploads = True
            self.standard_basic_email_campaigns = True
            self.standard_portfolio_showcase = True
            self.standard_standard_industry_resources = True
            self.standard_webinars_training_sessions = True
            # Premium Plan Features
            self.premium_order_tracking = True
            self.premium_customer_support = True
            self.premium_ai_powered_insights = True
            self.premium_integration_with_ai_tools = True
            self.premium_custom_reports = True
            self.premium_marketing_campaign

s = True
            self.premium_gallery_and_portfolio = True
            self.premium_training_and_resources = True
            self.price = 20.0

        return super().save(*a, **kw)

    def __str__(self):
        return f"subscription-{self.shop}"
```

## Usage

### API Endpoints

#### 1. Get List of Subscription Plans

- **Endpoint:** `/api/v1/plans/`
- **Method:** `GET`
- **Description:** Retrieve a list of available subscription plans.

#### 2. Subscribe to a Plan

- **Endpoint:** `/api/v1/subscribe/`
- **Method:** `POST`
- **Description:** Subscribe to a specific plan.

   **Request Body:**
   ```json
   {
       "plan_type": "standard",
       "shop_owner": 1,
   }
   ```

### Implementation Details

Upon submission of the above data to the specified endpoint, the view begins a series of checks on the data. The first check is to verify if the request was a `POST` request to the server. If this request is not as expected, the server returns with an `HTTP 400` status code and a "Method not allowed" error message.

The data is then extracted from the request:
```python
    plan_type = data["plan_type"]
    user_id = data["shop_owner"]
```

The following checks are made:

1. **Check if the plan type is valid:**
    ```python
    # Check plan type is valid
    valid_plans = ["basic", "standard", "premium"]
    if plan_type not in valid_plans:
        return Response({"error": "Invalid Plan, valid plans include: [basic, standard, premium]"}, status=status.HTTP_400_BAD_REQUEST)
    ```

    If an invalid plan type is sent in the request body, the system responds with an `HTTP 400 BAD REQUEST` status code and a message indicating that the plan was invalid, along with the list of valid plans.

2. **Check if the user exists:**
    ```python
    # Check if user exists, since the system just takes in the user ID, any number could be sent
    try:
        user_instance = get_object_or_404(User, pkid=user_id)
    except User.DoesNotExist:
        return Response({"error": "User with the given ID not found"}, status=status.HTTP_400_BAD_REQUEST)
    ```

    This ensures the existence of the user in the system, as any number could be sent as the user ID.

3. **Check if the user already has a current subscription:**
    ```python
    # Check if the user already has a current subscription
    subscription_exists = Subscription.objects.filter(shop_owner=user_id, plan_type=plan_type)
    if subscription_exists.exists():
        return Response({"error": "Current user already has a subscription with the same plan"}, status=status.HTTP_400_BAD_REQUEST)
    ```

    If the user already has a subscription of the same type, the system responds with an appropriate error message.

4. **Check if the user already has any form of subscription:**
    ```python
    # Check if the user already has any form of subscription
    subscription_exists = Subscription.objects.filter(shop_owner=user_id)
    if subscription_exists.exists():
        return Response({"error": "User cannot switch subscriptions on this route. To upgrade your subscription, go to http://localhost:8000/api/v1/subscriptions/upgrade/"}, status=status.HTTP_400_BAD_REQUEST)
    ```

    If the user already has any form of subscription, the system responds with a message directing the user to upgrade their subscription.

When all these checks have been successfully made and passed, the serializer instance is created, checked for validation, and then the subscription plan is created.

```python
serializer = SubscriptionCreateSerailizer(data=data)
if serializer.is_valid():
    # Perform payment....
    serializer.save()
    subscription = Subscription.objects.get(shop_owner=user_id)
    # Create a shop for this subscription
    shop = Shop.objects.create(
        user=User.objects.get(pkid=user_id),
        subscription=subscription,
    )
    shop.save()
    return Response({"message": "success"}, status=status.HTTP_200_OK)
else:
    return Response({"error": "Something went wrong!"})
```

After creating a serializer, a shop is automatically created in the system for the associated subscription. This shop instance has no information, so the frontend should redirect the user to the form page where they can update their shop details as needed.

When all this is done, an `HTTP 200 OK` status code is returned with a success message.

#### 3. View User's Subscription

- **Endpoint:** `/api/v1/plans/subscription/`
- **Method:** `GET`
- **Description:** Retrieve information about the user's current subscription.

The following code explains how this is achieved using the Django REST framework serializers:

```python
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def

 user_subscription_details(request):
    user = request.user
    subscription = Subscription.objects.filter(shop_owner=user)
    if subscription.exists():
        subscription = subscription.first()
        serializer = SubscriptionListSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Current logged-in user has no subscription available"})
```

## Examples

### Subscribe to a Plan

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <user_token>" -d '{"plan_type": "standard", "shop_owner": 1}' http://your-api-url/api/v1/plans/subscribe/
```

## Considerations

- The `AUTH_USER_MODEL` is properly configured for the project.
- Payment and billing processes are properly configured.

## Future Enhancements

- Integrate with a payment gateway for automated billing.
- Implement a trial period for new users.