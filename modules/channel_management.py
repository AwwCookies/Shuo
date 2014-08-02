## SHUO MODULE ##
"""
Channel Management

Version: 1.0.0
Author: Emma Jones (AwwCookies)

Desc:
Add channel management funcations to Shuo
"""
class SH_MODULE(sh.Module):
    def __init__(self):
        sh.Module.__init__(self)
        self.admins = [] + OTHER['OWNER']
        self.cmd_prefix = '@'
        self.hosts = {}

    def _allowed(self, host):
        if host in self.admins:
            return True
#-------------------------------------------#
    def kick(self, nick, msg='GO AWAY.'):
        sock.send('KICK %s %s :%s\r\n' % (data['Channel'], nick, msg))

    def op(self, nick):
        set_mode(data['Channel'], '+o', nick)

    def deop(self, nick):
        set_mode(data['Channel'], '-o', nick)

    def voice(self, nick):
        set_mode(data['Channel'], '+v', nick)

    def devoice(self, nick):
        set_mode(data['Channel'], '-v', nick)

    def ban(self, nick):
        if nick in self.hosts:
            set_mode(data['Channel'], '+b', '*!*@' + self.hosts[data['Nick']])
        else:
            pass

    def unban(self, nick):
        if nick in self.hosts:
            set_mode(data['Channel'], '-b', '*!*@' + self.hosts[data['Nick']])
        else:
            pass

    def mute(self, nick):
        if nick in self.hosts:
            set_mode(data['Channel'], '+q', '*!*@' + self.hosts[data['Nick']])
        else:
            pass        

    def unmute(self, nick):
        if nick in self.hosts:
            set_mode(data['Channel'], '-q', '*!*@' + self.hosts[data['Nick']])
        else:
            pass 
#-------------------------------------------#
    def on_join(self, data):
        # Map nick to host
        self.hosts[data['Nick']] = data['Host'].split('@')[1]

    def on_message(self, data):
        # Map nick to host
        self.hosts[data['Nick']] = data['Host'].split('@')[1]

        if self._allowed(data['Host'].split('@')[1]):
            # Command: OP
            if startswith(data['Message'], self.cmd_prefix + 'op'):
                if len(data['Args']) > 1:
                    self.op(data['Args'][1])
                else:
                    self.op(data['Nick'])
            # Command: DEOP
            if startswith(data['Message'], self.cmd_prefix + 'deop'):
                if len(data['Args']) > 1:
                    self.deop(data['Args'][1])
                else:
                    self.deop(data['Nick'])
            # Command: Voice
            if startswith(data['Message'], self.cmd_prefix + 'voice'):
                if len(data['Args']) > 1:
                    self.voice(data['Args'][1])
                else:
                    self.voice(data['Nick'])
            # Command: Devoice
            if startswith(data['Message'], self.cmd_prefix + 'devoice'):
                if len(data['Args']) > 1:
                    self.devoice(data['Args'][1])
                else:
                    self.devoice(data['Nick'])
            # Command: Ban
            if startswith(data['Message'], self.cmd_prefix + 'ban'):
                if len(data['Args']) > 1:
                    self.ban(data['Args'][1])
                else:
                    self.ban(data['Nick'])
            # Command: Unban
            if startswith(data['Message'], self.cmd_prefix + 'unban'):
                if len(data['Args']) > 1:
                    self.unban(data['Args'][1])
                else:
                    self.unban(data['Nick'])
            # Command: Kick
            if startswith(data['Message'], self.cmd_prefix + 'kick'):
                if len(data['Args']) > 1:
                    self.kick(data['Args'][1])
            # Command: Kick-Ban
            if startswith(data['Message'], self.cmd_prefix + 'kickban'):
                if len(data['Args']) > 1:
                    self.ban(data['Args'][1])
                    self.kick(data['Args'][1])
            # Command: Mute
            if startswith(data['Message'], self.cmd_prefix + 'mute'):
                if len(data['Args']) > 1:
                    self.mute(data['Args'][1])
            # Command: Umute
            if startswith(data['Message'], self.cmd_prefix + 'unmute'):
                if len(data['Args']) > 1:
                    self.unmute(data['Args'][1])
        else:
            pass