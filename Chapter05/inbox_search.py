__author__ = 'Chetan'

import config, imaplib

# M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
# M.login(config.fromaddr, config.password)
# M.select("INBOX")
# typ, data = M.search(None, 'SUBJECT', "Email with an attachment")
# typs, msg = M.fetch(data[0].split()[-1], '(RFC822)')
# print "Message is ", msg[0][1]
# M.close()
# M.logout()


import gmail, config
from datetime import date
g = gmail.login(config.fromaddr, config.password)
mails = g.inbox().mail(after=date(2016, 7, 22))
mails[-1].fetch()
print "Email Body:\n", mails[-1].body
g.logout()

