## SHUO MODULE ##
"""

"""
import random

class CutTheWire(sh.Module):
    def __init__(self):
        sh.Module.__init__(self)
        self.name = "Cut the Wire"
        self.player = None
        self.wire = None
        self._kick = True
        self.start_time = None
        self.end_time = None
        self.ticks = 0
        self.channel = None
        self.nick = None
        self.wires = ['red', 'pink', 'gray', 'white', 'green']
        self.cmd_prefix = '-'

    def start_game(self, player, nick, channel):
        print player
        self.nick = nick
        self.channel = channel
        self.start_time = self.ticks
        self.end_time = self.start_time + 30
        self.player = player
        self.wire = random.choice(self.wires)
        send_message(channel, "%s, you have been tasked with disarming a bomb. %s" % (nick, self.wires))

    def end_game(self):
        self.player = None
        self.wire = None
        self.start_time = None
        self.end_time = None
        if self._kick:
            self.kick(self.nick, self.channel, 'BOOM!')

    def kick(self, nick, channel, msg=''):
        sock.send('KICK %s %s :%s\r\n' % (channel, nick, msg))

    def cut(self, wire):
        if wire == self.wire:
            self.end_game()
            send_message(self.channel, "%s disarms the bomb!" % self.nick)
        else:
            self.end_game()
            send_message(self.channel, "%s blows up!" % self.nick)

    def on_message(self, data):
        if startswith(data['Message'], self.cmd_prefix + 'ctw') and not self.player:
            self.start_game(data['Host'], data['Nick'], data['Channel'])
        elif startswith(data['Message'], self.cmd_prefix + 'ctw') and self.player:
            send_message(data['Channel'], 'Current player: (%s)' % self.player)

        if startswith(data['Message'], self.cmd_prefix + 'cut'):
            if data['Host'] == self.player:
                self.cut(data['Args'][1])
            else:
                send_message(data['Channel'], "Current player: %s" % self.player)

    def on_tick(self, ticks):
        self.ticks = ticks
        if self.player:
            if self.ticks > self.end_time:
                self.end_game()
                send_message(self.channel, "%s blows up!" % self.nick)
#-----#
module(CutTheWire)