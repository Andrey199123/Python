import smtplib
from email.mime.text import MIMEText
import time
html = open("email.html")
msg = MIMEText(html.read(), 'html')
msg['Subject'] = 'Help Andrey Vasilyev raise funds for Falcon Cove Middle School Debate'
msg['From'] = 'andrey999va@gmail.com'
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login("andrey999va@gmail.com", "ijdsrffyepfiyuai")
counter = 0
with open('emails.txt', 'r') as file:
    for line in file:
        msg['To'] = str(line)
        s.send_message(msg)
        print(line, counter)
        counter += 1
        if counter % 70 == 0:
            time.sleep(200)
s.quit()
