import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

email=EmailMessage()
#html=Template(Path('index.html').read_text())
email['from']="[Sender's Name]"
email['to']='[Email ID of the recepient]'
email['subject']='[Subject]'
email.set_content('[Content]')
#email.set_content(html.substitute({'name':'Tintin'}),'html')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('[Your Email]','[Your Password]')
    smtp.send_message(email)
    print('Email Sent')

# SMTP - SIMPLE MAIL TRANSFER PROTOCOL

