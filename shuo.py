## Shuo the better IRC bot
## Created by Emma Jones
## Version: 0.0.1 - July 30, 2014

import socket
import string
import os
import glob
import sh
import time
import getpass
from termcolor import cprint

execfile("./config.py")
running = True
readbuffer = ''
pretty_messages = True
#-------------------------#
db = {
    'Joined Channels': [],
    'FIRST_RUN': True,
    'commands': {},
    'modules': [],
    'MOTD': "",
    "ServerCap": "",
}
#--------Load Mods--------#
def module(mod_class, metadata=None):
    db['modules'].append(mod_class())
    print("Loaded module: %s" % (mod_class().name))

for folder in glob.glob('./modules/*/'):
    for mod in glob.glob(folder + '*.py'):
        with open(mod, 'r') as f:
            if f.readlines()[0].strip() == '## SHUO MODULE ##':
                execfile(mod)
#--Connect to IRC Server--#
def connect():
    cprint('Connecting to: %s as: %s' % (CONN_SETTINGS['Server'], BOT['Nick']), 'blue')
    global sock
    sock = socket.socket()  # Create a new socket
    if CONN_SETTINGS["BIND"] != "": sock.bind((CONN_SETTINGS["BIND"], 0))  # BIND to an IP 
    sock.connect((CONN_SETTINGS["Server"], CONN_SETTINGS["Port"]))  # Connect to the Server
    if CONN_SETTINGS["ServerPassword"] != "": sock.send("PASS " + CONN_SETTINGS["ServerPassword"] + "\r\n")  # Send Server password (if any)
    sock.send("NICK %s\r\n" % CONN_SETTINGS["Nick"])  # Tell the Server your nick
    sock.send("USER %s %s bla :%s\r\n" % (CONN_SETTINGS["Ident"], CONN_SETTINGS["Server"], CONN_SETTINGS["RealName"]))  # Tell the server your user info
connect()
#------------Basic Module Functions---------#
def log(msg, p = "info"):
    if p == "info":
        cprint("[info]: %s" % msg, 'grey')
    elif p == 'warning':
        cprint("[warning]: %s" % msg, 'yellow')

def register_commands(commands):
    pass

def startswith(string, word, splitby=' '):
    return string.split(splitby)[0] == word

def is_owner(host):
    return host.split('@')[1] in OTHER['OWNER']
#-------------Basic IRC Commands -----------#
def set_mode(channel, mode, nick):
    sock.send("MODE %s %s %s\r\n" % (channel, mode, nick)) ## Sent Mode
    log('(set_mode) Setting %s on %s in %s' % (mode, nick, channel), 'info')

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

def send_message(channel, message, bypass=False):
    if channel in OTHER['Approved Channels'] or bypass:
        sock.send('PRIVMSG %s :%s\r\n' % (channel, message))
        log("send_message [bypass = %s]: Sending a message to %s - (%s)." % (bypass, channel, message))
    else:
        log("send_message: Attempted to send a message to %s but it is not in the approved channel list", 'warning')

def do_action(channel, message, bypass=False):
    if channel in OTHER['Approved Channels'] or bypass:
        sock.send('PRIVMSG %s :\x01ACTION %s\x01\r\n' % (channel, message))
        log("send_message [bypass = %s]: Sending a message to %s - (%s)." % (bypass, channel, message))
    else:
        log("send_message: Attempted to send a message to %s but it is not in the approved channel list", 'warning')

def send_notice(channel, message, bypass=False):
    if channel in OTHER['Approved Channels'] or bypass:
        sock.send('NOTICE %s :%s\r\n' % (channel, message))
        log("send_message [bypass = %s]: Sending a message to %s - (%s)." % (bypass, channel, message))
    else:
        log("send_notice: Attempted to send a notice to %s but it is not in the approved channel list", 'warning')
#--------------Built in Modules-------------#
def autojoin():
    for channel in OTHER['Autojoin']:
        join_channel(channel)

def nickserv_auth():
    '''Auths you with nickserv'''
    send_message('NickServ', 'IDENTIFY %s' % OTHER['NickServ'], True)
#-------------------------------------------#
if not os.path.exists("modules"):
    os.mkdir("modules")
#-------------------------------------------#
while running:
    time.sleep(0.1)
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
        if data['Host'] == '372':
            db['MOTD'] += data['Message']
        elif data['Host'] == '001':
            db['ServerCap'] += data['Message']
        else:
            if pretty_messages:
                if data['Type'] == 'JOIN':
                    cprint('(%s (%s) joined -> %s)' % (data['Nick'], data['Host'], data['Channel']), 'blue')
                elif data['Type'] == 'PART':
                    cprint('(%s (%s) left <- %s)' % (data['Nick'], data['Host'], data['Channel']), 'green')
                elif data['Type'] == 'NOTICE':
                    cprint('%s (%s) send you a notice: %s)' % (data['Nick'], data['Host'], data['Message']), 'magenta')
                elif data['Type'] == 'MODE':
                    cprint('(%s (%s) set mode %s in %s)' % (data['Nick'], data['Host'], data['Message'], data['Channel']), 'yellow')
                elif data['Type'] == 'PRIVMSG':
                    cprint('(%s (%s) in %s said: %s)' % (data['Nick'], data['Host'], data['Channel'], data['Message']), 'cyan')
                elif data['Type'] == 'KICK':
                    kicked = data['Message'].split(' :')[0]
                    reason = data['Message'].split(' :')[1]
                    cprint('(%s (%s) kicked %s from %s because: %s' % (data['Nick'], data['Host'], kicked, data['Channel'], reason), 'red')
                else:
                   print data
            #else:
                #print data
    except:
        pass
    #-------------------------------#
    # Prompt to choose new nick if current one is already being used.
    if data['Type'] == '*' and 'Nickname is already in use.' in data['Message']:
        cprint("%s is already being used. Please choose a new nick." % BOT['Nick'], 'red')
        change_nick(str(raw_input('Nick: ')))

    if db['FIRST_RUN']:
        nickserv_auth()
        autojoin()
    #------------Modules------------#
    try:
        for mod in db['modules']:
            data['Args'] = data['Message'].split() 
            if data['Type'] == 'PRIVMSG': mod.on_message(data);
            if data['Type'] == 'PART': mod.on_part(data);
            if data['Type'] == 'JOIN': mod.on_join(data);
            if data['Type'] == 'NOTICE': mod.on_notice(data);
            if data['Type'] == 'NICK': mod.on_nick(data);
            if data['Type'] == 'MODE':
                data['Mode'] = data['Message'].split()[0]
                mod.on_mode(data);
            if data['Type'] == 'KICK': 
                data['Kicked'] = data['Message'].split(' :')[0]
                data['Reason'] = data['Message'].split(' :')[1]
                mod.on_kick(data)
    except Exception, e:
        print(e.message)
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