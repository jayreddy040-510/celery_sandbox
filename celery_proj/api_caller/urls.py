from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import test_view

urlpatterns = [
    path('test_url', csrf_exempt(test_view), name='test-view')
        ]
