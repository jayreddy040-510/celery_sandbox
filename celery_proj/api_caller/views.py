from django.shortcuts import render
from .tasks import test
from django.http import HttpResponse

def test_view(request):
    print("inside the view")
    if request.method == 'POST':
        test.delay()
        return HttpResponse("http request done")
