from django.shortcuts import render
from .tasks import test

def test(request):
    test.delay()
    return HttpResponse("http request done")
