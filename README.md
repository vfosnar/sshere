# sshere
 Python3 script for automating ssh to a directory on a sftp network drive
## Usage
    # Mount the sftp system
    sshfs user@example.com:/ /home/localuser/example
    
    # cd into the mounted fs
    cd /home/localuser/example
    
    # And start sshere
    sshere
    
    # This will ask for password and open / on the server
#### sshpass support. if you can use keys instead, please
    # First install sshpass
    # Debian: sudo apt install sshpass
    # Arch: pacman -S sshpass
    
    # edit config.json and change config to
    {
        "user@example.com":{"passwd":"super secret password"}
    }
    
    # It will login to the server automatically

## How-to install
    # Clone this repo
    git clone https://github.com/vfosnar/sshere.git
    cd sshere
    
    # Edit config to match your own ssh servers
    nano ./config.json
    
    # Add sshere alias to the bashrc file
    make install
    
    # and restart console
