## SHUO MODULE ##

"""
Tell

Version: 1.0.0
Author: Emma Jones (AwwCookies)

Desc:
Tell Shuo to relay a message to a user.
"""

import time
import json
import os


class Tell(sh.Module):
    def __init__(self):
        sh.Module.__init__(self)
        if os.path.exists('./tell.json'):
            self.pending_messages = json.loads(open('./tell.json').read())
        else:
            self.pending_messages = {}
        self.cmd_prefix = '@'

    def _save(self):
        with open('./tell.json', 'w') as f:
            f.write(json.dumps(self.pending_messages))

    def add_msg(self, nick, message, channel):
        if self.pending_messages.get(nick):
            self.pending_messages[nick].append({'msg': message, 'chan': channel})
        else:
            self.pending_messages[nick] = [{'msg': message, 'chan': channel}]
        self._save()

    def rem_msg(self, nick):
        del self.pending_messages[nick]
        self._save()

    def on_message(self, data):
        if self.pending_messages.get(data['Nick'].lower()):
            for msg in self.pending_messages[data['Nick'].lower()]:
                channel = msg.get('chan')
                message = msg.get('msg')
                send_message(channel, message)
            self.rem_msg(data['Nick'].lower())
        if startswith(data['Message'], self.cmd_prefix + 'tell'):
            if len(data['Args']) > 1:
                self.add_msg(data['Args'][1].lower(), '<' + data['Nick'] + '> ' + ' '.join(data['Message'].split()[2:]) , data['Channel'])
                send_message(data['Channel'], sh.color('Okay', 'blue'))
#-----------------#
module(Tell, 'Tell')
