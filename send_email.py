from secure import username, password
import smtplib


def send_email(content):
    # Login to Gmail  and authenticate
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(username, password)

    # Generate and send the e-mail
    subject = "This is s a test"
    body = content

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(username, username, msg)
    print("Email has been sent")

    # Close Gmail connection
    server.quit()

