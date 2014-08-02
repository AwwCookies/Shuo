## GINGERSNAP MODULE ##
class GS_MODULE(gs.Module):
    def __init__(self):
        gs.Module.__init__(self)
        self.cmd_prefix = "@"

    def on_message(self, data):
        if startswith(data['Message'], self.cmd_prefix + 'test'):
            sock.send('WHOIS Aww\r\n')

    def on_mode(self, data):
        send_message(data['Channel'], '%s set %s' % (data['Nick'], data['Mode']))