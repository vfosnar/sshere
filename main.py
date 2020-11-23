servers = {
    "name@example.com":{"port":2222},
    "name2@example2.com":{"passwd":"examplepass", "win":True}
}

import os

mnt = os.popen("df --output=source .").read().split('\n')[1]
tar = os.popen("df --output=target .").read().split('\n')[1]

addr = mnt.split(":")[0]
base = ":".join(mnt.split(":")[1:])

server = os.path.join(base, os.getcwd()[len(tar):][1:])

port = 22
passwd = None
win = False

if(addr in servers):
    if("port" in servers[addr]):
        port = servers[addr]['port']
    if("passwd" in servers[addr]):
        passwd = servers[addr]['passwd']
    if("win" in servers[addr]):
        win = servers[addr]['win']
    

ssh = 'ssh -t {} -p {} "cd \\"{}\\"; bash --login"'

if(win): # Is computer running on windows
    ssh = 'ssh -t {} -p {} cmd /K "cd "{}""'
    server = server[1:]
    if(server[-1] != '/'):
        server += '/'

if(passwd): # sudo apt install sshpass
    os.system('sshpass -p {} '.format(passwd) + ssh.format(addr, port, server))
    pass
else:
    os.system(ssh.format(addr, port, server))