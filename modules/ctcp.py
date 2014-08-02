## SHUO MODULE ##
"""
Client To Client Protocal 

Version: 1.0.0
Author: Emma Jones (AwwCookies)

Desc:
Allows Shuo to reply to CTCP's
"""

import time

class SH_MODULE(sh.Module): 
    def __init__(self):
        sh.Module.__init__(self)
        self.replies = {
            'Version': 'Shuo, Version: 0.0.1 (https://github.com/AwwCookies/Shuo) Created by Emma Jones (AwwCookies)',
        }

    def on_message(self, data):
        if '\x01' in data['Message']:
            if 'VERSION' in data['Message'].upper():
                send_notice(data['Nick'], self.replies['Version'], True)
            elif 'TIME' in data['Message'].upper():
                send_notice(data['Nick'], time.time(), True)
            elif 'PING' in data['Message'].upper():
                send_notice(data['Nick'], "\x01PING %s\x01" % ' '.join(data["Message"].replace("\x01","").split()[1:]), True)
