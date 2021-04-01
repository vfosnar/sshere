import os, json, sys

def log(text: str, error: bool = False):
    if(error):
        sys.stdout.write("\e[B")
    print("[sshere]", text)
    if(error):
        sys.stdout.write("\e[0m")
        exit(1)

if __name__ == "__main__":
    # Load config file
    servers = {}
    
    configPath = os.path.join(os.path.dirname(__file__), 'config.json')
    if(os.path.exists(configPath)):
        with open(configPath, 'r', encoding="utf-8") as file:
            servers = json.loads(file.read())
        
    # name@address:/path/on/server
    serverMountTag = os.popen("df --output=source .").read().split('\n')[1]
    # /local/mount/path
    localMountPath = os.popen("df --output=target .").read().split('\n')[1]

    if(serverMountTag[:len('/dev')] == '/dev'):
        log("Filesystem must be a SFTP, make sure you are in the right directory.", True)
    # name@address
    serverAddress = serverMountTag.split(":")[0]
    
    # /path/on/server
    serverMountPath = ":".join(serverMountTag.split(":")[1:])

    # Get current working directory and strip out mount point
    # [1:] -> get rid if / on the beggining and thus make it relative path
    relativeCWD = os.getcwd()[len(localMountPath):][1:]

    # Change it to absolute path by adding server path to the mount point
    serverCWD = os.path.join(serverMountPath, relativeCWD)

    # Defaults
    port = 22
    passwd = None
    win = False

    serverConfigName = None
    
    # Check if name@address is in the config
    if(serverAddress in servers):
        serverConfigName = serverAddress
    
    # Check if name@address:/local/path is in the config
    elif("{}:{}".format(serverAddress, localMountPath) in servers):
        serverConfigName = "{}:{}".format(serverAddress, localMountPath)

    # Load ssh configuration from config.json
    if(serverConfigName):
        if("port" in servers[serverConfigName]):
            port = servers[serverConfigName]['port']
        if("password" in servers[serverConfigName]):
            passwd = servers[serverConfigName]['password']
        if("windows" in servers[serverConfigName]):
            win = servers[serverConfigName]['windows']
        
        if("passwd" in servers[serverConfigName]):
            log("Using 'passwd' is deprecated, use 'password' instead.")
            passwd = servers[serverConfigName]['passwd']
        if("win" in servers[serverConfigName]):
            log("Using 'win' is deprecated, use 'windows' instead.")
            win = servers[serverConfigName]['win']
        
    # command used to connect to the linux server
    ssh = 'ssh -t {} -p {} "cd \\"{}\\"; bash --login"'

    if(win):
        # When the server computer is running windows
        # we need to change the shell command
        ssh = 'ssh -t {} -p {} cmd /K "cd /d "{}""'
        if(serverCWD == "/"):
            log("Can't ssh into / of a Windows computer.", True)
        # We need to patch CWD because windows filesystem uses 'C:' and not '/C:'
        serverCWD = serverCWD[1:]
        # We must also patch the / at the end because Windows won't cd into 'C:', it must be 'C:/'
        if(serverCWD[-1] != '/'):
            serverCWD += '/'

    log("Connecting to {} at a port {}.".format(serverAddress, port))
    if(passwd):
        # User defined password in the config.json file.
        # This should not be used but I needed it so here it goes.
        # We call sshpass with user's password and our ssh command:
        os.system('sshpass -p "{password}" {ssh}'.format(
            password = passwd,
            ssh = ssh.format(serverAddress, port, serverCWD)
            ))
    else:
        # User wants interactive login or uses a ssh keypair.
        # Anyways we just call the ssh command:
        os.system(ssh.format(serverAddress, port, serverCWD))