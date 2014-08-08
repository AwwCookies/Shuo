## SHUO MODULE ##
"""
Corrections

Version: 1.0.0
Author: Emma Jones (AwwCookies)
"""

class Correction(sh.Module):
    def __init__(self):
        sh.Module.__init__(self)
        self.messages = {}
        self.name = "Corrections"

    def on_message(self, data):
        if data['Message'].startswith('s/'):
            correction = self.messages[data['Nick']].replace(data['Message'].split('/')[1], data['Message'].split('/')[2])
            send_message(data['Channel'], data['Nick'] + ', meant to say: ' + correction)
        else:
            self.messages[data['Nick']] = data['Message']
#------#
module(Correction)