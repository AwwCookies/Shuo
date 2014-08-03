## SHUO MODULE ##
"""
Ask

Version: 1.0.0
Author: Emma Jones (AwwCookies)

Example: @ask Go to sleep or Stay on IRC
This will return either "Go to sleep" or "Stay on IRC"
"""

import random

class Ask(sh.Module):
    def __init__(self):
        sh.Module.__init__(self)
        self.cmd_prefix = "@"

    def ask(self, string):
        return random.choice(string.split('or'))

    def on_message(self, data):
        if startswith(data['Message'], self.cmd_prefix + 'ask'):
            send_message(data['Channel'], self.ask(' '.join(data['Message'].split()[1:])).strip())

#--------#
module(Ask, 'Ask')