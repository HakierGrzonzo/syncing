#!/usr/bin/python3
import datetime, os

def notify():
    message = """
To: admin@grzegorzkoperwas.site
From: grzes869@gmail.com
Subject: Suspicious activity on ryzenRig

Someone logged in at {} 
    """.format(datetime.datetime.now())
    print(message)
    with open("/tmp/warn.mail", "w+") as mail:
        mail.write(message)
    os.system('bash -c "cat /tmp/warn.mail | msmtp -a default admin@grzegorzkoperwas.site"')


work_hours = 6, 13

now = datetime.datetime.now()
if now.weekday() in range(6):
    if work_hours[0] < now.hour < work_hours[1]:
        notify()
