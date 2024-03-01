from django.contrib import admin
from django.urls import path, include
from apps.common.views import test_send_mail, js_test_rout
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path("testmail/", test_send_mail, name="send-mail"),
    path("api/test/", js_test_rout),
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    # path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/customers/", include("apps.customers.urls", namespace="customers")),
    path("api/v1/orders/", include("apps.orders.urls", namespace="orders")),
    path("api/v1/shops/", include("apps.shop.urls", namespace="shop")),
    path("api/v1/plans/", include("apps.subscriptions.urls", namespace="subscriptions")),
    path("api/v1/gallery/", include("apps.gallery.urls", namespace="gallery")),
    path("api/v1/reviews/", include("apps.reviews.urls", namespace="reviews")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)