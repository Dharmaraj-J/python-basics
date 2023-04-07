from email.message import EmailMessage
import ssl,smtplib

email_sender = input("enter your email :")
email_password = input('enter your email password :')
email_reciver = input('enter your reciver email :')

subject = "project D"

body = '''
finish the project within 10 days.
'''

em = EmailMessage()
em['From'] = email_sender
em['To']  = email_reciver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciver)