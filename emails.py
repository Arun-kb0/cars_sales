from re import sub
import smtplib
import mimetypes
from email.message import EmailMessage
import os

def genrate_email(sender,recipient, subject, body, attachment, pswd):
    message = EmailMessage()
    message['from']= sender
    message['to']= recipient
    message['subject']= subject
    message.set_content(body)

    filename =os.path.basename(attachment)
    mime,_=mimetypes.guess_type(filename)
    mime_type,mime_subtype = mime.split('/')
   

    with open(attachment, 'rb') as ap:
        message.add_attachment(ap.read(),
        maintype= mime_type,
        subtype= mime_subtype,
        filename = os.path.basename(attachment),
        )

        print("message ok")

    server= smtplib.SMTP_SSL('smtp.google.com')
    #server.login(sender,pswd)
    #print('login successfull')
    #server.sendmail(sennder,recipient, message)
    #server.quit()