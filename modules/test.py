## SHUO MODULE ##
"""

"""

class SH_MODULE(sh.Module):
    def __init__(self):
        sh.Module.__init__(self)

    def on_message(self, data):
        if startswith(data['Message'], '~hug'):
            do_action(data['Channel'], '(>^.^)>')