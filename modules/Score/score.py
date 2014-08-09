## SHUO MODULE ##
"""
Score

Version 1.0.0
Author: Emma Jones (AwwCookies)
"""

import os
import json


class Score(sh.Module):
    def __init__(self):
        sh.Module.__init__(self)
        self.cmd_prefix = '@'
        self.name = 'Score'
        if os.path.exists('./scores.json'):
            self.scores = json.loads(open('./scores.json').read())
        else:
            self.scores = {}

    def _save(self):
        with open('./scores.json', 'w') as f:
            f.write(json.dumps(self.scores))

    def add_point(self, nick, data):

        nick = nick.lower()
        if self.scores.get(data['Channel']):
            if self.scores[data['Channel']].get(nick):
                self.scores[data['Channel']][nick] += 1
            else:
                self.scores[data['Channel']][nick] = 1
        else:
            self.scores[data['Channel']] = {nick: 1}
        self._save()
        return self.scores[data['Channel']][nick]

    def rem_point(self, nick, data):
        nick = nick.lower()
        if self.scores.get(data['Channel']):
            if self.scores[data['Channel']].get(nick):
                self.scores[data['Channel']][nick] -= 1
            else:
                self.scores[data['Channel']][nick] = -1
        else:
            self.scores[data['Channel']] = {nick: -1}
        self._save()
        return self.scores[data['Channel']][nick]

    def on_message(self, data):
        if startswith(data['Message'], '+point'):
            if len(data['Args']) > 1:
                send_message(data['Channel'], data['Args'][1] + ': ' + str(self.add_point(data['Args'][1], data)))
        elif startswith(data['Message'], '-point'):
            if len(data['Args']) > 1:
                self.rem_point(data['Args'][1], data)
                send_message(data['Channel'], data['Args'][1] + ': ' + str(self.rem_point(data['Args'][1], data)))
        elif startswith(data['Message'], self.cmd_prefix + 'points'):
            if len(data['Args']) > 1:
                send_message(data['Channel'], str(self.scores[data['Channel']][data['Args'][1].lower()]))
#----------#
module(Score)