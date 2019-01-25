import smtplib
import string
#import boto3
#from botocore.exceptions import ClientError
def read_file():
    contents=open('smtppythonliborg.py','r')
    return '<br/>'.join(contents.readlines())
f = open('smtppythonliborg.py','r')
message = f.read()
print(message)
f.close()
HOST = "smtp.gmail.com"
SUBJECT = "Test email from Python library org blog"
TO = "recepentemail"
FROM = "fromemail"
text = "Python rules them all! daily and hourly email report"
BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        message
        ), "\r\n")
server = smtplib.SMTP(HOST, 587)
#server.ehlo()
server.starttls()
#server.ehlo()
server.login(FROM, "password")
server.sendmail(FROM, [TO], BODY)
server.quit()



