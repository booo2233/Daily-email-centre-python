from app.api_email_send import *
import pprint
import schedule
import time

email_uesr_email = None
while True:
    try:
        uesr_email = input("Enter your email: ")
        uesr,host = uesr_email.split("@")
    except ValueError:
        print("=====(Invalid-email)======")
        continue
    else:
        email_uesr_email = str(email_uesr_email)
        print(uesr, host)
        email_uesr_email = uesr_email
        break



def email_send_you_use():
     email_gmail(email_uesr_email)
  
     

schedule.every().day.at("10:30").do(email_uesr_email)

while True:
    schedule.run_pending()
    time.sleep(1)
