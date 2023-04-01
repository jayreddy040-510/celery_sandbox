from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import test_view, test_sleep_view, test_group_view

urlpatterns = [
        path('test_url', csrf_exempt(test_view), name='test-view'),
        path('test_sleep_url', csrf_exempt(test_sleep_view), name='test-sleep-view'),
        path('group_task_url', csrf_exempt(test_group_view), name='test-group-view')
        ]
