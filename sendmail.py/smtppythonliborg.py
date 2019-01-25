import smtplib
import string
 
HOST = "smtp.gmail.com:465"
SUBJECT = "Test email from Python library org blog"
TO = "yrprasadprasad@gmail.com"
FROM = "yrprasadprasad@gmail.com"
text = "Python rules them all! daily and hourly email report"
BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        text
        ), "\r\n")
server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], BODY)
server.quit()