#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails
import sys

def process_data(directory):
    fruit_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r') as f:
                tempList = []
                tempList = f.read().split('\n')
                dict = {
                    'name': tempList[0],
                    'weight': tempList[1]
                }
                fruit_list.append(dict)

    return fruit_list

def main(argv):
    directory = ''
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    report_title = "Processed Update on "+d1
    fruit = process_data(directory)
    paragraph = ""
    for x in fruit:
        temp = "name: " + x["name"] + "<br/>" + "weight:" + x["weight"] + "<br/><br/>"
        paragraph = paragraph + temp

    reports.generate('/tmp/processed.pdf', report_title, paragraph)

    #send the PDF report as an email attachment
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body ="All fruits are uploaded to our website successfully. A detailed list is attached to this email"
    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send(message)


if __name__ == "__main__":
    main(sys.argv)