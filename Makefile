install:
	echo 'alias sshere="python3 $(dir $(realpath $(firstword $(MAKEFILE_LIST))))main.py"' >> ~/.bashrc
	@echo "[sshfs] Added to the ~/.bashrc"
	@echo "[sshfs] Please restart console before using!"