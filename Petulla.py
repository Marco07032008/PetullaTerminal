#!/usr/bin/env python3

import subprocess
import os
import sys
import time

def install_figlet():
    # Check if figlet is installed
    result = subprocess.run(["which", "figlet"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Installing figlet...")
        subprocess.run(["sudo", "apt", "install", "figlet", "-y"])

def main():
    # Check if the script is run with root privileges
    if os.geteuid() != 0:
        print("You must run this as root!")
        sys.exit(1)

    # Install figlet if not already installed
    install_figlet()

    # Display a message using figlet
    subprocess.run(["figlet", "Petulla Terminal"])

    # Wait for 5 seconds
    time.sleep(5)

    # Clone zphisher repository
    subprocess.run(["git", "clone", "--depth=1", "https://github.com/htr-tech/zphisher.git"])

    # Wait for another 5 seconds
    time.sleep(5)

    # Change directory to zphisher
    os.chdir("zphisher")

    # Wait for 2 seconds
    time.sleep(2)

    # Run zphisher.sh
    subprocess.run(["bash zphisher.sh"])

if __name__ == "__main__":
    main()
