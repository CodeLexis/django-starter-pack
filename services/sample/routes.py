from django.urls import path

from rest_framework import routers

from .views import HelloView


router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns += [
    path('hello', HelloView.as_view(), name='hello'),
]
