import smtplib
import ssl
import csv
import time

#Modify your details
sender_email = "ADD_YOUR_EMAIL"
password = "ADD_YOUR_PASSWORD"

#Modify Subject and Content
message = """\
Subject: Fet Subject

Dear {name},

You bring back the Fet or I won't Fet Like you anymore!
You better have ma' Fetty!
"""



with open('recipients.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)  # skip header row
    
    for row in csv_reader:
        name = row[0]
        email = row[1]

        message_formatted = message.format(name=name)

        # set up SMTP server
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)

            # send email
            server.sendmail(sender_email, email, message_formatted.encode("utf-8"))

            # wait for 10 seconds before sending the next email
            time.sleep(5)