from django.shortcuts import render
from .tasks import test

def test_view(request):
    test.delay()
    return HttpResponse("http request done")
