import smtplib
from dating.email_pass import login, password


def email_sender(email_recipient, text):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.starttls()
    smtpobj.login(login, password)
    smtpobj.sendmail(login, email_recipient, text)
    smtpobj.quit()
