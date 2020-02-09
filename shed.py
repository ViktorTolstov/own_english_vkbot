from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import vk
import time
import math
import database
import requests

now = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
print(now)

session = vk.Session(access_token='99a11e00502987b24bcb91adc963708fd2c264f5143d4f8bbd1a25549b1fb34f003371ca7a3c36dd76ad0')
vk_api = vk.API(session)

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=15, minute=34)  # запускать c понедельника по пятницу в 10.00
def scheduled_job():
    post = requests.get('http://localhost:5000/get_db').json()
    random_id = int(round(time.time()))
    attachment = ""
    for index in post["attachments"]:
        attachment += index + ","
    vk_api.messages.send(chat_id=1, message=post["text"],attachment=attachment, random_id=random_id,v=5.103)
    print('This job is run every weekday at 10am.')

# scheduled_job()
sched.start()