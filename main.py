import os, json

# Load config file
servers = json.loads(open(os.path.join(os.path.dirname(__file__), 'config.json'), 'rb').read().decode())

if __name__ == "__main__":
    # name@address:/path/on/server
    mnt = os.popen("df --output=source .").read().split('\n')[1]
    # /local/mount/path
    tar = os.popen("df --output=target .").read().split('\n')[1]

    if(mnt[:len('/dev')] == '/dev'):
        print("Only sftp is supported..")
        exit(1)
    # name@address
    addr = mnt.split(":")[0]
    
    # /path/on/server
    base = ":".join(mnt.split(":")[1:])

    # Get current working directory and strip out mount point
    # [1:] -> get rid if / on the beggining and thus make it relative path
    rels = os.getcwd()[len(tar):][1:]

    # Change it to absolute path by adding server path to the mount point
    server = os.path.join(base, rels)

    # Defaults
    port = 22
    passwd = None
    win = False

    servers_name = None
    
    # Check if name@address is in the config
    if(addr in servers):
        servers_name = addr
    
    # Check if name@address:/local/path is in the config
    elif("{}:{}".format(addr, tar) in servers):
        servers_name = "{}:{}".format(addr, tar)

    # Load ssh configuration from config.json
    if(servers_name):
        if("port" in servers[servers_name]):
            port = servers[servers_name]['port']
        if("passwd" in servers[servers_name]):
            passwd = servers[servers_name]['passwd']
        if("win" in servers[servers_name]):
            win = servers[servers_name]['win']
        
    # command used to connect to the linux server
    ssh = 'ssh -t {} -p {} "cd \\"{}\\"; bash --login"'

    if(win): # Is computer running on windows
        # windows has different syntax
        ssh = 'ssh -t {} -p {} cmd /K "cd /d "{}""'
        # Win filesystem begins with C: not /C:
        server = server[1:]
        if(len(server) == 0):
            print("Can't ssh into / of windows computer!")
            exit(1)
        # Windows wont cd into C: must be C:/
        if(server[-1] != '/'):
            server += '/'

    print("Connecting to {} at port {}".format(addr, port))
    # if passwd is specified in config.json file then sshpass is used
    # sshpass must be already installed:
    #  sudo apt install sshpass
    if(passwd):
        os.system('sshpass -p {} '.format(passwd) + ssh.format(addr, port, server))
        pass
    else:
        os.system(ssh.format(addr, port, server))