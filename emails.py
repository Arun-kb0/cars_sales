from posixpath import basename
from re import sub
import smtplib
import mimetypes
from email.message import EmailMessage
import os

def genrate_email(sender,recipient, subject, body, attachment,attachment2, pswd):
    print('\ngenerating message....')
   
    message = EmailMessage()
    message['from']= sender
    message['to']= recipient
    message['subject']= subject
    message.set_content(body)

    #cars pdf 
    filename =os.path.basename(attachment)
    mime,_=mimetypes.guess_type(filename)
    mime_type,mime_subtype = mime.split('/')
    
    with open(attachment, 'rb') as ap:
        message.add_attachment(ap.read(),
        maintype= mime_type,
        subtype= mime_subtype,
        filename = os.path.basename(attachment),
        )
    #line chart
    filename2= os.path.basename(attachment2)
    mime2,tmp= mimetypes.guess_type(filename2)
    mime_type2,mime_subtype2= mime2.split('/')
    with open(attachment2, 'rb') as ap2:
        message.add_attachment(ap2.read(),
        maintype= mime_type2,
        subtype= mime_subtype2,
        filename= os.path.basename(attachment2)
        )

    #print(message)
    print('sending mail....')
    try:
        server= smtplib.SMTP_SSL('smtp.google.com')
        server.login(sender,pswd)
        print('login successfull !')
        server.sendmail(sender,recipient, message)
        print('email sended !')
        server.quit()
    except TimeoutError:
        print('failed to send email !')
        print('tip : check your google account security settings')