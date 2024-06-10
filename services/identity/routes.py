from django.urls import path

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import SignupView, UserViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register('users', UserViewSet, 'users')

urlpatterns = router.urls

urlpatterns += [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup', SignupView.as_view(), name='signup'),
]
