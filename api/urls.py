from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from .views import UserViewSet, SummarizeTextViewSet

# router 
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('summarize-text', SummarizeTextViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

