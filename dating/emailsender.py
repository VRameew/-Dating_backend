import smtplib
import email_pass


def email_sender(email_recipient, text):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.starttls()
    smtpobj.login(email_pass.login, email_pass.password)
    smtpobj.sendmail(email_pass.login, email_recipient, text)
    smtpobj.quit()
