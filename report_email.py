#!/usr/bin/env python3

import os
import datetime
import reports
import emails

def buildParagraph(descriptionFilesDir):
    descriptionFiles = os.listdir(descriptionFilesDir)

    paragraph = ""
    for descriptionFile in descriptionFiles:
        f = open("{}/{}".format(descriptionFilesDir,descriptionFile), 'r')
        description = f.readlines()
        paragraph = "{}name: {}\nweight: {}\n\n".format(paragraph, 
                                                        description[0].rstrip('\n'),
                                                        description[1].rstrip('\n'))
    return paragraph

if __name__ == "__main__":
    user = os.getenv("USER")
    descriptionFilesDir = "/home/{}/supplier-data/descriptions".format(user)
    
    # Create report
    paragraph = buildParagraph(descriptionFilesDir)
    title = "Processed Update on {}".format(datetime.date.today().strftime("%d/%m/%y"))
    
    fileDestination = "/tmp/processed.pdf"
    
    reports.generate_report(fileDestination, title, paragraph)
    
    # Send report by email
    email_subject = 'Upload Completed - Online Fruit Store'
    email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    
    msg = emails.generate_email("automation@example.com", "{}@example.com".format(user),
                         email_subject, email_body, "/tmp/processed.pdf")
    emails.send_email('localhost', msg)
