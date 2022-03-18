__author__ = 'Chetan'

import gmail, config
g = gmail.login(config.fromaddr, config.password)
emails = g.inbox().mail(sender='junk@xyz.com')
if emails:
    for mail in emails:
        mail.delete()

