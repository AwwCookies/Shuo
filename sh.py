class Module:
    def __init__(self):  # Called when the bot first starts up
        self.name = "Unnamed Module"

    def on_message(self, data):  # Called when a message is send to a channel 
        # data:
            # Nick: Nick of the user talking
            # Host: Host of the user talking
            # Channel: Channel in which, the user is talking in
            # Type: Will always be PRIVMSG for on_message()
            # Message: What the person said
            # Args: The message split by spaces
        pass

    def on_part(self, data):  # Called when someone leaves a channel
        pass

    def on_join(self, data):  # Called when someone joins a channel
        pass

    def on_notice(self, data):  # Called when someone sends you a notice
        pass

    def on_mode(self, data):  # Called when a mode is changed in a channel
        pass

    def on_nick(self, data):  # Called when someone changes their nick
        pass

    def on_kick(self, data):  # Called when someone gets kicked from a channel
        pass

    def on_tick(self, data):  # Called every second
        pass

    def __del__(self):  # Called when the bot is shutdown
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