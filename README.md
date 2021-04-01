# sshere
 Python3 script for automating ssh into a server based on CWD in a SFTP network drive
## Usage
Navigate into the SFTP filesystem
```bash
sshfs user@example.com:/ /home/localuser/sftp
cd /home/localuser/sftp/subdirectory
```

And run ``sshere``. This will find the mount point, compare it to the CWD and ssh you into the server. You will end up in the ``/subdirectory`` on the server.
This script also works with mount other than root directory.

## Installation
```bash
git clone https://github.com/vfosnar/sshere.git
cd sshere

make install
```

## Config file
Config file contains dictionary of ``serverName`` as a key and a dictionary specifying ``options`` as a value.
The ``options`` can be ``port: int``, ``windows: bool`` and ``password: str``\
So for example at the server side, we have a ``user`` named ``serveruser`` and the ``server`` is ``example.org``. We want to specify port 2222 because else it will default to 22. It is also a windows computer so we must specify it too.
```json
{
    "serveruser@example.org": {"port": 2222, "windows": true}
}
```
We can also specify a password for ssh. For security reasons you should use ssh keys instead!
This requires a ``sshpass`` package to be installed
```json
{
    "serveruser@example.org": {"port": 2222, "windows": true, "password": "MySup3rSecr3tP4s5w0rd"}
}
```
More examples of ``config.json`` file are in [_config.json](/_config.json)
