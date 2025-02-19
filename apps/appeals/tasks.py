import time

from celery import shared_task

@shared_task
def generate_excel_file():
    print('generate_excel_file in 5 minutes')
    time.sleep(60*5)