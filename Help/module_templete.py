# Gingersnap module templete file

#-------------------------------#

class GS_MODULE(module.Module):  # Class MUST be called GS_MODULE
    def __init__(self):
        module.Module.__init__(self)
    def on_message(self, data):
        pass

    def on_part(self, data):
        pass

    def on_join(self, data):
        pass

    def on_notice(self, data):
        pass