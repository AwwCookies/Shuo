## Shuo the better IRC bot
## Created by Emma Jones
## Version: 0.0.1 - July 30, 2014

import socket
import string
import os
import glob
import gs
execfile("./config.py")
running = True
readbuffer = ''
#-------------------------#
db = {
    'Joined Channels': [],
    'FIRST_RUN': True,
    'commands': {}
}
#-------------------------#
# Connect to IRC Server

def connect():
    global sock
    sock = socket.socket()  # Create a new socket
    if CONN_SETTINGS["BIND"] != "": sock.bind((CONN_SETTINGS["BIND"], 0))  # BIND to an IP 
    sock.connect((CONN_SETTINGS["Server"], CONN_SETTINGS["Port"]))  # Connect to the Server
    if CONN_SETTINGS["ServerPassword"] != "": sock.send("PASS " + CONN_SETTINGS["ServerPassword"] + "\r\n")  # Send Server password (if any)
    sock.send("NICK %s\r\n" % CONN_SETTINGS["Nick"])  # Tell the Server your nick
    sock.send("USER %s %s bla :%s\r\n" % (CONN_SETTINGS["Ident"], CONN_SETTINGS["Server"], CONN_SETTINGS["RealName"]))  # Tell the server your user info
connect()

#-------------------------------------------#
def log(msg, p = "info"):
    if p == "info":
        print("[info]: %s" % msg)

def register_commands(commands):
    pass

def startswith(string, word, splitby=' '):
    return string.split(splitby)[0] == word

def set_mode(channel, mode, nick):
    sock.send("MODE %s %s %s\r\n" % (channel, mode, nick)) ## Sent Mode
    log('(set_mode) Setting %s on %s in %s' % (mode, nick, channel), 'info')
#-------------Basic IRC Commands -----------#
def join_channel(channel):
    '''Joins the bot to a channel.'''
    sock.send("JOIN %s\r\n" % channel)
    log("join_channel: Joining channel '%s'" % channel, 'info')
    db['Joined Channels'].append(channel)

def part_channel(channel):
    '''Parts the bot from a channel.'''
    sock.send("PART %s\r\n" % channel)
    log("part_channel: Parting channel '%s'" % channel, 'info')
    db['Joined Channels'].remove(channel)

def change_nick(nick):
    ''' Change the nick of the bot.'''
    log('(change_nick) changing nick to: %s' % nick)
    sock.send('NICK %s\r\n' % nick)
    ABOUT["BotName"] = nick

def send_message(channel, message, bypass=False):
    if channel in OTHER['Approved Channels'] or bypass:
        sock.send('PRIVMSG %s :%s\r\n' % (channel, message))
        log("send_message: Sending a message to %s - (%s)." % (channel, message))
    else:
        log("send_message: Attempted to send a message to %s but it is not in the approved channel list")
#--------------Built in Modules-------------#
def autojoin():
    for channel in OTHER['Autojoin']:
        join_channel(channel)
#-------------------------------------------#
if not os.path.exists("modules"):
    os.system("mkdir modules")
#-------------------------------------------#
while running:
    readbuffer += sock.recv(1024)
    tempdata = readbuffer.replace("!", " !").split()
    try:
        data = {
            "Nick":tempdata[0].lstrip(":"),
            "Host":tempdata[1].replace("!", ""),
            "Type":tempdata[2],
            "Channel":tempdata[3],
            "Message":' '.join(tempdata[4:]).lstrip(":")
        }
        print data
    except:
        pass
    #-------------------------------#
    if db['FIRST_RUN']:
        autojoin()
    #------------Modules------------#
    for mod in glob.glob('./modules/*.py'):
        m = open(mod)
        if m.readlines()[0].strip() == '## GINGERSNAP MODULE ##':
            data['Args'] = data['Message'].split() 
            execfile(mod)
            if data['Type'] == 'PRIVMSG': GS_MODULE().on_message(data);
            if data['Type'] == 'PART': GS_MODULE().on_part(data);
            if data['Type'] == 'JOIN': GS_MODULE().on_join(data);
            if data['Type'] == 'NOTICE': GS_MODULE().on_notice(data);
            if data['Type'] == 'MODE':
                data['Mode'] = data['Message'].split()[0]
                GS_MODULE().on_mode(data)
        else:
            print("%s does not have '## GINGERSNAP MODULE ##' header." % mod)
        m.close()
    #-------------------------------#

    data = {"Nick":"NULL", "Host":"NULL", "Type":"NULL", "Channel":"NULL", "Message":"NULL"}
    tempdata = ""
    db['FIRST_RUN'] = False
    ###########################
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()

    for line in temp:
        line = string.rstrip(line)
        line = string.split(line)

        if(line[0]=="PING"):
            sock.send("PONG %s\r\n" % line[1])