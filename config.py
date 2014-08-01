## Config file for Shuo "The better IRC Bot"
## Created by Emma Jones

BOT = {
    "Nick": 'Shuo'
}

CONN_SETTINGS = {
    "Server": "irc.freenode.net", # Example: "chat.freenode.net"
    "ServerPassword": "", # Example: "password"; leave blank if there is no server password
    "Port": 6667, # 6667
    "Ident": BOT['Nick'], # Example: "Gingersnap"
    "Nick": BOT['Nick'], # Example: "Gingersnap"
    "RealName": BOT['Nick'], # Example: "Gingersnap"
    'BIND': '' # Bind to an IP; leave blank if you do not wish to bind to an IP Example: '66.55.152.127'
}

OTHER = {
    "Autojoin": ["##Aww-Bot"],
    'CMD_PREFIX': '>',
    'Approved Channels': ['##Aww-Bot']
}