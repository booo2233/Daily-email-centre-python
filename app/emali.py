import ssl
from email.message import EmailMessage
import smtplib

def email(subject, body, emil_receiver):

 emil_sender = "youarealoafofbread1@gmail.com"
 emil_password = "itrs achj pquo fezj"
  
 
 em = EmailMessage()
 em["From"] = emil_sender
 em["to"] = emil_receiver
 em["Subject"] = subject
 em.set_content(body)

 context = ssl.create_default_context()
 

 with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    smtp.login(emil_sender,emil_password)
    smtp.sendmail(emil_sender,emil_receiver,em.as_string())

 