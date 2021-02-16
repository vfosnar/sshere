# sshere
 Python3 script for automating ssh to a directory on a sftp network drive
## Usage
    # mount the sftp system
    sshfs user@example.com:/ /home/localuser/example
    
    # cd into the mounted fs
    cd /home/localuser/example
    
    # and start sshere
    # this will ask for password and open "/" on the server
    sshere
    
    # Exit shell to exit ssh
    exit
    
    # cd to some subdirectory
    cd subdir
    
    # sshere to server
    # this will open "/subdir" cwd in server shell
    sshere
    
#### sshpass support. if you can use keys instead, please
    # first install sshpass
    # Debian: sudo apt install sshpass
    # Arch: pacman -S sshpass
    
    # edit config.json and change config to
    {
        "user@example.com":{"passwd":"super secret password"}
    }
    
    # now it will auth to the server automatically

## How-to install
    # Clone this repo
    git clone https://github.com/vfosnar/sshere.git
    cd sshere
    
    # Edit config to match your own ssh servers
    nano ./config.json
    
    # Add sshere alias to the bashrc file
    make install
    
    # and restart console
