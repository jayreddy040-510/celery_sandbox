from celery import shared_task
import time

@shared_task(bind=True)
def test(self):
    for i in range(10):
        print(i)
    return "done"

@shared_task
def sleeper_task(x):
   time.sleep(x)
   print(f"slept for blah")
   return x
