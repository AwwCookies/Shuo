## SHUO MODULE ##

"""
Actions

Version: 1.0.0
Author: Emma Jones (AwwCookies)

Desc:
"""

class Actions(sh.Module):
    def __init__(self):
        sh.Module.__init__(self)
        self.cmd_prefix = '~'
        self.actions = {
            'hug': '(>^.^)> $nick'
        }

    def parse(self, text, data):
        return text.replace('$nick', data['Nick'])

    def on_message(self, data):
        if data['Message'].startswith(self.cmd_prefix):
            if data['Message'].replace(self.cmd_prefix, '') in self.actions:
                do_action(data['Channel'], self.parse(self.actions[data['Message'].replace(self.cmd_prefix, '')], data))
#--------#
module(Actions, 'Actions')