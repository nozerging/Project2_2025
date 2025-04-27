import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage
from datetime import datetime, timedelta
from_email_addr = "3906994157@qq.com"
from_email_pass = "superccs75"
to_email_addr = "1976729868@qq.com"

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def send_email(water_status):
    msg = EmailMessage()
    body = "I need water" if not water_status else "I don't need water"
    msg.set_content(body)
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['Subject'] = 'Plant'

    server = smtplib.SMTP('smtp.qq.com', 587)
    server.starttls()
    server.login(from_email_addr, from_email_pass)
    server.send_message(msg)
    print('Email sent:', body)
    server.quit()

def check_water_status():
    return GPIO.input(channel)
def wait():
    while True:
        now = datetime.now()
        if now.hour == 7 and now.minute == 0:
            return
        time.sleep(60)
email_count = 0
wait() 
while email_count < 4: 
    water_detected = check_water_status()
    send_email(water_detected)
    email_count += 1
 
    if email_count < 4:
        time.sleep(3 * 60 * 60)
