from secure import *
import smtplib


def send_email(msg):
    # Login to Gmail  and authenticate
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(username, password)

    # Generate and send the e-mail
    subject = "This is s a test"
    body = "Check the Amazon Link"

    server.sendmail(username, username, msg)
    print("Email has been sent")

    server.quit()

