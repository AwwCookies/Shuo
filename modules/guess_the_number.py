## SHUO MODULE ##

"""
Guess the number!

Version: 1.0.0
Author: Emma Jones (AwwCookies)

Desc: Guess the number between 0 and 100

Commands: 
    -gtn (Starts a game)
    -guess (Take a guess)
    -quit (End the game)
"""

import random

class GTN(sh.Module):
    def __init__(self):
        sh.Module.__init__(self)
        self.player = None
        self.cmd_prefix = '-'
        self.number = random.randint(0, 100)
        self.running = False

    def start_game(self, host):
        print self.number
        self.player = host
        self.running = True

    def end_game(self):
        self.running = False
        self.player = None

    def on_message(self, data):
        if self.running:
            if data['Host'] == self.player:
                if startswith(data['Message'], self.cmd_prefix + 'guess'):
                    if int(data['Args'][1]) == self.number:
                        send_message(data['Channel'], 'Correct!')
                        self.end_game()
                    elif int(data['Args'][1]) < self.number:
                        send_message(data['Channel'], 'Higher!')
                    elif int(data['Args'][1]) > self.number:
                        send_message(data['Channel'], 'Lower!')
                elif data['Message'] == self.cmd_prefix + 'quit':
                    self.end_game()
            elif startswith(data['Message'], self.cmd_prefix + 'guess'):
                send_message(data['Channel'], '%s is currently playing.' % self.player)
        elif startswith(data['Message'], self.cmd_prefix + 'gtn'):
            self.start_game(data['Host'])
            send_message(data['Channel'], 'Guess the number! Player: %s' % data['Host'])
#------#
module(GTN, 'Guess the number')

