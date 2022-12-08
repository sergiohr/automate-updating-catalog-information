#!/usr/bin/env python3
from email.message import EmailMessage
import mimetypes
import smtplib
import os

def generate_email(sender, recipient, subject, body, attachment_path = None):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    
    message.set_content(body)
    
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    
    if attachment_path != None:
        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=os.path.basename(attachment_path))
    
    return message

def send_email(mailServer, message):
    mailServer = smtplib.SMTP(mailServer)
    mailServer.send_message(message)
    mailServer.quit()
