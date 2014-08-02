## SHUO MODULE ##

#-------------------------------#

class SH_MODULE(sh.Module):
    def __init__(self):
        sh.Module.__init__(self)
    def on_message(self, data):
        pass

    def on_part(self, data):
        pass

    def on_join(self, data):
        pass

    def on_notice(self, data):
        pass

    def on_mode(self, data):
        pass

#----------#
db['modules'].append(SH_MODULE())