__author__ = 'Chetan'

import smtplib
import config

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(config.fromaddr, config.password)

msg = "Some nice msg"
server.sendmail(config.fromaddr, config.toaddr, msg)
server.verify(config.fromaddr)
server.quit()
