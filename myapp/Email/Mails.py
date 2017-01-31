# host, gmail.smtp.com
# port: 587
#user_name:
#password:

import smtplib

sender = 'user@mail.com'
receiver = ['receiver@mail.com']

message = 'Hello, this is test mail'

try:
    smtpObj = smtplib.SMTP('host', 'port')
    smtpObj.sendmail(sender, receiver, message)
    print('Email sent successfully')
except:
    print('Exception occured while sending email')
