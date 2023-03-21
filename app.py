from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'redwankibria73@gmail.com'
email_password = ''

email_receiver = ''
subject = 'You got this bro!'
body = """
you know you NEVER GIVE UP.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


# for email_password, generate two factor app password from google account setting
# for email_reciever, I have used temp-mail site to generate random disposable email id
# if the email goes to temp-mail id mail inbox, that means the code is running.
