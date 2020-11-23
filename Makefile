install:
	echo 'alias sshere="python3 $(dir $(realpath $(firstword $(MAKEFILE_LIST))))main.py"' >> ~/.bashrc