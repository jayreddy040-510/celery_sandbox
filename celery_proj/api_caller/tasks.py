from celery import shared_task
import time

@shared_task(bind=True)
def test(self):
    for i in range(10):
        print(i)
        time.sleep(2)
    return "done"
