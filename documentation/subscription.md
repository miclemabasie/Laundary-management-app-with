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
- `SubscriptionCreateSerailizer`: Serializes subscription data for API interactions (Used only for creating Subscriptions instances in the system).
- `SubscriptionListSerializer`: Handles data serialization for listing out subscriptions through the API.
- `create_subscription`: Handles API endpoints for subscribing to a subscription plan.
- `list_subscriptions`: Handles API endpoints for listing out all subscription plans.
- `user_subscription_details`: Handles API endpoints for retreiving all subscription information about the currently logged in user.


### Data Models

#### SubscriptionPlan Model

``` python
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
        # Auto fill in the transactioni id
        self.transaction_id = str(uuid.uuid4())[-17:]
        # Calulate and save prices based on plan choice
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
            self.premium_marketing_campaigns = True
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
On submission of the above data to the specified enpoint, the view begins a series of checks on the data, the first check made is to double check inside the code if the request was actually a ```POST``` request to the server, if this request is not what we expect, then the server returns with an ```HTTP 400``` status code with a ```Method not allowed``` error message.
The data is after then extrapulated from the request as shown below
```python
    plan_type = data["plan_type"]
    user_id = data["shop_owner"]
```
when the data has been gotten from the request, the following checks are made

Check if the plan type is a one of those supported by the system
```python
   # Check plan type is valid
    valid_plans = ["basic", "standard", "premium"]
    if plan_type not in valid_plans:
        return Response({"error": "Invalid Plan, valid plans include, [basic, standard, premium]"}, status=status.HTTP_400_BAD_REQUEST)
```
As seen on the code if a none valid plan type is sent in the request body, for example
  **Request Body:**
   ```json
   {
       "plan_type": "testplan",
       "shop_owner": 1,
   }
   ```
Then the system will respond with an ```HTTP_400_BAD_REQUEST``` status code with a message to indicate that the plan was invlid and also presents the following valid plans that can be used to make a valid request.

After this check is made, we move on to chceck the existence of the use in the system, since we rely on the frontend to send us a request with a valid userID alot of things can go wrong in this case, so we safely check to see if the user exists just as a counter measure incase any funny request was made to the server, the code snippet below shows exacly how this is done

```python
# Check if user exist, since the system just takes in the userid, any number could be sent
try:
    user_instance = get_object_or_404(User, pkid=user_id)
except User.DoesNotExist:
    return Response({"error": "User with id not found"}, status=status.HTTP_400_BAD_REQUEST)
```

Since we do not want the user to perform a subscription of the same kind if there already have any, we make a check to m make sure that the user does not try to subscribe to the same plan twice, this is done using the following code.
```python
# Check if user already has a current subsciption
subscription_exists = Subscription.objects.filter(shop_owner=user_id, plan_type=plan_type)
if subscription_exists.exists():
    return Response({"error": "Current User already has a subscription with same plan"}, status=status.HTTP_400_BAD_REQUEST)
```
as seen on the code above, we get a subscription which is owned by the userID that was sent in the request body and has the same plan type as sent in the request body, if this subsciption instance already exists, then we respond with an appropriate error message indicating what exactly is going on.

Last but not the least, a check is made if the user already has a subscription plan of any type, in this case if a user happens to have a subscription plan of anykind, then the system response with an appropriate error message indicating the user on where to go to to find information for upgrading their plan
```python 
# Check if user already has any form of subscriptioin
subscription_exists = Subscription.objects.filter(shop_owner=user_id)
if subscription_exists.exists():
    return Response({"error": "user can not switch subscriptions on this route, to upgrade your subscription, go to http://localhost:8000/api/v1/subscriptions/upgrade/"})
```

When all the checks have been successfuly made and all passed, the serializer instance is created, checked for validation and then the subscription plan is being created
```python
serializer = SubscriptionCreateSerailizer(data=data)
if serializer.is_valid():
    # Perform payment....
    serializer.save()
    subscription = Subscription.objects.get(shop_owner=user_id)
    # Create shop for this 
    shop = Shop.objects.create(
        user = User.objects.get(pkid=user_id),
        subscription = subscription,
    )
    shop.save()
    return Response({"message": "success"}, status=status.HTTP_200_OK)
else:
    return Response({"error": "something went wrong!"})
```

as seen in the code after creating a serializer, a shop is automatically created in the system for the associated subscription, this shop instance has not information and so then the frontend should make sure that it redirects the user to the form page were they can update their shop details as need.

when all this is done, an ```HTTP_200_OK``` status code is returned with a success message.


#### 3. View User's Subscription

- **Endpoint:** `/api/v1/plans/subscription/`
- **Method:** `GET`
- **Description:** Retrieve information about the user's current subscription.

The following code self explains how this is achieved using the restframework serializers
```python
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def user_subscription_details(request):
    user = request.user
    subscription = Subscription.objects.filter(shop_owner=user)
    if subscription.exists():
        subscription = subscription.first()
        serializer = SubscriptionListSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Current logged in user has no subscription available"})
```



## Examples

### Subscribe to a Plan

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <user_token>" -d '{"plan_type": "standard", "shop_owner": 1}' http://your-api-url/api/v1/plans/subscribe/
```

## Considerations

- The `AUTH_USER_MODEL` is properly configured for the project.
- Payment and billing processes are properly configured 

## Future Enhancements

- Integrate with a payment gateway for automated billing.
- Implement a trial period for new users.


