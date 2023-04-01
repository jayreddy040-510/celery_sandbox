from django.shortcuts import render
from celery import chain, group
from django.http import HttpResponse
from .tasks import sleeper_task, group_task, test

def test_view(request):
    if request.method == 'POST':
        test.delay()
        return HttpResponse("http request done")

def test_sleep_view(request):
    if request.method == 'POST':
        task_chain = chain(
            sleeper_task.si(num) for num in range(4)        
                )
        task_chain.apply_async()
        return HttpResponse("ugh let me sleep")

def test_group_view(request):
    if request.method == 'POST':
        tasks = [
            group_task(num).s() for num in range(5)
                ]
        task_group = group(tasks)
        task_group.apply_async()
