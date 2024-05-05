import time
from app.emali import *
import requests,random,pprint,json

count = 0

def email_gmail(use_emails):
 while True:
  ran = random.randrange(2,4)
  url = "https://www.boredapi.com/api/activity" 
  request = requests.get(url,{"participants":ran})


  ur = request.text
  info = json.loads(ur)
  if not info or "activity" not in info:
      continue
  else:  
    info = info["activity"] 
  #time.sleep(2)
 
  api = info
  global count
  subject = f"Day {count} Sending email so you don't get bored"
  count = int(count)
  if api == "" or subject == "" or api == None:
    print("😒😒")
    print(api)
    continue

  else:
       email(subject,api,use_emails)
       count = count + 1
       print(count)

















