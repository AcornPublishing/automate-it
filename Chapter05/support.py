__author__ = 'Chetan'

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import config, time, gmail

def send_email(strTo):
    strFrom = config.fromaddr
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Thanks for your ticket'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo

    msgRoot.preamble = 'This is a multi-part message in MIME format.'
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)
    msgText = MIMEText('Hi there, <br><br>Thanks for your query with us today.'
                       ' You can look at our <a href="https://google.com">FAQs</a>'
                       ' and we shall get back to you soon.<br><br>'
                       'Thanks,<br>Support Team<br><br><img src="cid:image1">', 'html')
    msgAlternative.attach(msgText)
    fp = open('google.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(config.fromaddr, config.password)
    server.sendmail(config.fromaddr, config.toaddr, msgRoot.as_string())
    server.quit()

while True:
    g = gmail.login(config.fromaddr, config.password)
    mails = g.inbox().mail(unread=True)
    mails[-1].fetch()
    from_ = mails[-1].fr
    send_email(from_)
    time.sleep(60)


