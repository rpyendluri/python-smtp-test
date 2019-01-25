import smtplib
import string

def send_email(host, subject, to_addr, from_addr, body_text):
    """
    Send an email
    """
    def read_file():
        contents=open('report.txt','r')
        return '<br/>'.join(contents.readlines())
    BODY = string.join((
            "From: %s" % from_addr,
            "To: %s" % to_addr,
            "Subject: %s" % subject ,
            "",
            body_text
            ), "\r\n")
    server = smtplib.SMTP(host)
    server.sendmail(from_addr, [to_addr], BODY)
    server.quit()


#import boto3
#from botocore.exceptions import ClientError
def read_file():
    contents=open('report.txt','r')
    return '<br/>'.join(contents.readlines())
HOST = "smtp.gmail.com"
SUBJECT = "Test email from Python library org blog"
TO = "receipentemail.com"
FROM = "fromemail.com"
text = "Python rules them all! daily and hourly email report"
BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        text
        contents
        ), "\r\n")
server = smtplib.SMTP(HOST, 587)
#server.ehlo()
server.starttls()
#server.ehlo()
server.login(FROM, "password")
server.sendmail(FROM, [TO], BODY)
server.quit()
