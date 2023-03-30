from django.shortcuts import render
from celery import chain
from .tasks import test
from django.http import HttpResponse
from .tasks import sleeper_task

def test_view(request):
    if request.method == 'POST':
        test.delay()
        return HttpResponse("http request done")

def test_sleep_view(request):
    if request.method == 'POST':
        task_chain = chain(
            sleeper_task.s(num) for num in range(4)        
                )
        task_chain.apply_async()
        return HttpResponse("ugh let me sleep")
