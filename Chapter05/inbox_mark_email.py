__author__ = 'Chetan'


import gmail, config
g = gmail.login(config.fromaddr, config.password)
mails = g.inbox().mail(unread=True, sender='noreply@glassdoor.com')
mails[-1].fetch()
mails[-1].read()
g.logout()

import gmail, config
from datetime import date
g = gmail.login(config.fromaddr, config.password)
mails = g.inbox().mail(unread=True, sender='store-news@amazon.in',
                       after=date(2016, 01, 01))
for email in mails:
    email.read()
    email.add_label("AMAZON")
g.logout()

