## SHUO MODULE ##
"""

"""

class Shuo(sh.Module):
    def __init__(self):
        self.name = "Shuo"
        self.cmd_prefix = '$'

    def loaded_modules(self):
        return [x.name for x in db['modules']]

    def on_message(self, data):
        if is_owner(data['Host']):
            if startswith(data['Message'], self.cmd_prefix + 'modules'):
                send_message(data['Channel'], "Loaded modules: %s" % self.loaded_modules())
#------#
module(Shuo)