from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'blog', BlogViewSet)
router.register(r'services', ServicesViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'portfolio', PortfolioViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
