## SHUO MODULE ##
"""
Log

Version: 1.0.0
Author: Emma Jones (AwwCookies)
"""

import time

class Logs(sh.Module):
    def __init__(self):
        sh.Module.__init__(self)

    def on_message(self, data):
        with open('./logs.csv', 'a') as f:
            f.write('%s, %s, %s, %s, %s, %s\n' % (str(time.time()), data['Nick'], data['Host'], data['Type'], data['Channel'], data['Message']))
#--------#
module(Logs, 'Logs')