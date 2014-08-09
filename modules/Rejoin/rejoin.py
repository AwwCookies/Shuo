## SHUO MODULE ##
"""
Rejoin

Version: 1.0.1
Author: Emma Jones (AwwCookies)
"""

class Rejoin(sh.Module):
    def __init__(self):
        sh.Module.__init__(self)
        self.name = 'Rejoin'

    def on_kick(self, data):
        if data['Kicked'] == BOT['Nick']:
            join_channel(data['Channel'])
#-----#
module(Rejoin)