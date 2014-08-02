class Module:
    def __init__(self):
        pass

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

def color(text, c):
    colors = {
        'white': '\x0300',
        'black': '\x0301',
        'blue': '\x0302',
        'green': '\x0303',
        'red': '\x0304',
        'brown': '\x0305',
        'purple': '\x0306',
        'orange': '\x0307',
        'yellow': '\x0308',
        'light green': '\x0309',
        'teal': '\x0310',
        'light cyan': '\x0311',
        'light blue': '\x0312',
        'pink': '\x0313',
        'grey': '\x0314',
        'light grey': '\x0315',
        'bold': '\x02',
    }
    return(colors[c] + text + colors[c])
