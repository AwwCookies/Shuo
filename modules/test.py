## GINGERSNAP MODULE ##
class GS_MODULE(module.Module):
    def __init__(self):
        module.Module.__init__(self)
        self.cmd_prefix = "@"

    def on_message(self, data):
        if startswith(data['Message'], self.cmd_prefix + 'test'):
            GS['Send Message'](data['Channel'], 'Hello, World')

    def on_join(self, data):
        GS['Send Message'](data['Channel'], "Hello, %s!" % data['Nick'])

    def on_part(self, data):
        GS['Send Message'](data['Channel'], "Aww... So sad to see them go.. :(")