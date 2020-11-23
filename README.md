# sshere
 Python script for automating ssh to a directory on a sftp network drive
## Usage
     # Mount the sftp system
     sshfs user@example.com:/ /home/localuser/example
     # cd into it
     cd /home/localuser/example
     # And start sshere
     sshere
     # This will ask for password and open / on the server
#### sshpass support
     # If you install sshpass like this
     sudo apt install sshpass
     
     # edit main.py and change config to
     #
     # servers = {"user@example.com":{"passwd":"super secret password"}}
     #
     # It will login to the server automatically

## How-to install
     # Clone this repo
     git clone https://github.com/vfosnar/sshere.git
     cd sshere
     
     # Open ./main.py
     # edit the servers config to match your own ssh servers
     sudo nano ./main.py
     
     # and save it
     # Open ~/.bashrc file
     sudo nano ~/.bashrc
     
     # add this line to the end of it (Don't forget to change the path!)
     alias sshere="python3 /path/to/the/cloned/repo/main.py"
     
     # Save the file and restart console
